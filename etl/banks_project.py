import requests, pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from etl.extract_top_banks import populate_top_banks_df
from etl.transform_top_banks import convert_usd
from sqlite_connection_manager.sqlite_connection_manager import SqliteConnectionManager


data_url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
exchange_rates_path = "./data/exchange_rate.csv"

top_banks_df = pd.DataFrame(
    columns=[
        "Bank_name",
        "Global_Data_Rank",
        "Global_Data_Market_cap_(USD_Billion)",
        "Forbes_India_Rank",
        "Forbes_India_Market_cap_(USD_Billion)",
    ]
)


def execute_using_sql_connection(operation, *args):
    with SqliteConnectionManager() as sql_connection:
        return operation(sql_connection, *args)


def log_progress(message):
    time_format = "%Y-%h-%d-%H:%M:%S"
    current_date = datetime.now()
    time_stamp = current_date.strftime(time_format)

    with open("code_log", "a") as log_file:
        log_file.write(f"""{time_stamp} : {message}\n""")


def extract(data_url, top_banks_df):
    html_page = requests.get(data_url).text
    html_data = BeautifulSoup(html_page, "html.parser")
    html_tables = html_data.find_all("tbody")
    html_rows = html_tables[2].find_all("tr")
    log_progress("Preliminaries complete. Initiating ETL process")
    return populate_top_banks_df(html_rows, top_banks_df)


def transform(top_banks_df, csv_path):

    for df_column_name in [
        "Global_Data_Market_cap_(USD_Billion)",
        "Forbes_India_Market_cap_(USD_Billion)",
    ]:
        top_banks_df = convert_usd(top_banks_df, df_column_name, csv_path)

    print(top_banks_df)
    log_progress("Data transformation complete. Initiating Loading process")
    return top_banks_df


def load_to_csv(transformed_df, output_path):
    transformed_df.to_csv(output_path)
    log_progress("Data saved to CSV file")


def load_to_db(sql_connection, top_banks_df, table_name):
    log_progress("SQL Connection initiated")
    top_banks_df.to_sql(table_name, sql_connection, if_exists="replace")
    log_progress("Data loaded to Database as a table, Executing queries")


def run_query(query_statement, sql_connection):
    """This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing."""

    log_progress("Process Complete")
    sql_connection.close()
    log_progress("Server Connection closed")


top_banks_df = extract(data_url, top_banks_df)
log_progress("Data extraction complete. Initiating Transformation process")
top_banks_df = transform(top_banks_df, exchange_rates_path)
load_to_csv(top_banks_df, "./output_data/largest_banks_data.csv")
table_name = "Largest_banks"
execute_using_sql_connection(load_to_db, top_banks_df, table_name)
