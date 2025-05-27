import requests, sqlite3, pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

data_url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
table_df = pd.DataFrame(
    columns=[
        "Bank_name",
        "Global_Data_Rank",
        "Global_Data_Market_cap_(USD_Billion)",
        "Forbes_India_Rank",
        "Forbes_India_Market_cap_(USD_Billion)",
    ]
)


def log_progress(message):
    time_format = "%Y-%h-%d-%H:%M:%S"
    current_date = datetime.now()
    time_stamp = current_date.strftime(time_format)

    with open("code_log", "a") as log_file:
        log_file.write(time_stamp + "," + message + "\n")


def get_bank_names(html_rows):
    bank_names = []

    for row in html_rows:
        cells = row.find_all("td")
        row_content = cells[0].find_all("a") if cells else []

        if len(row_content) > 1:
            bank_names.append(row_content[1].contents[0])

    return bank_names


def populate_table_df(html_rows, table_df):
    bank_names = get_bank_names(html_rows)
    row_index = 0

    for row in html_rows:
        cells = row.find_all("td")

        if cells:
            row_dict = {
                "Bank_name": bank_names[row_index],
                "Global_Data_Rank": cells[1].contents[0][:-1],
                "Global_Data_Market_cap_(USD_Billion)": cells[2].contents[0][:-1],
                "Forbes_India_Rank": cells[3].contents[0][:-1],
                "Forbes_India_Market_cap_(USD_Billion)": cells[4].contents[0][:-1],
            }

            row_df = pd.DataFrame(row_dict, index=[0])
            table_df = pd.concat([table_df, row_df], ignore_index=True)
            row_index += 1

    return table_df


def extract(table_df):
    html_page = requests.get(data_url).text
    html_data = BeautifulSoup(html_page, "html.parser")
    html_tables = html_data.find_all("tbody")
    html_rows = html_tables[2].find_all("tr")
    return populate_table_df(html_rows, table_df)


table_df = extract(table_df)
table_df.to_csv("output_data/largest_banks_data.csv")
