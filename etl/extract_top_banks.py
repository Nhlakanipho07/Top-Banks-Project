import pandas as pd


def get_bank_names(html_rows):
    bank_names = []

    for row in html_rows:
        cells = row.find_all("td")
        row_content = cells[0].find_all("a") if cells else []

        if len(row_content) > 1:
            bank_names.append(row_content[1].contents[0])

    return bank_names


def populate_top_banks_df(html_rows, top_banks_df):
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
            top_banks_df = pd.concat([top_banks_df, row_df], ignore_index=True)
            row_index += 1

    print(top_banks_df)
    return top_banks_df
