import pandas as pd, requests
from logs.log_progress import log_progress
from bs4 import BeautifulSoup


def get_html_rows(data_url):
    html_page = requests.get(data_url).text
    html_data = BeautifulSoup(html_page, "html.parser")
    html_tables = html_data.find_all("tbody")
    return html_tables[0].find_all("tr")


def get_bank_names(html_rows):
    bank_names = []

    for row in html_rows:
        cells = row.find_all("td")
        row_content = []
        if cells:
            row_content = cells[1].find_all("a")[1]["title"]

        if len(row_content) > 1:
            bank_names.append(row_content)

    return bank_names


def populate_top_banks_df(html_rows, top_banks_df):
    bank_names = get_bank_names(html_rows)
    row_index = 0

    for row in html_rows:
        cells = row.find_all("td")

        if cells:
            row_dict = {
                "Rank": int(cells[0].contents[0][:-1]),
                "Bank_name": bank_names[row_index],
                "Market_cap_(USD_Billion)": float(cells[2].contents[0][:-1]),
            }

            row_df = pd.DataFrame(row_dict, index=[0])
            top_banks_df = pd.concat([top_banks_df, row_df], ignore_index=True)
            row_index += 1

    log_progress("Data extraction complete. Initiating Transformation process")
    return top_banks_df


def extract(data_url, top_banks_df):
    html_rows = get_html_rows(data_url)
    log_progress("Preliminaries complete. Initiating ETL process")
    return populate_top_banks_df(html_rows, top_banks_df)
