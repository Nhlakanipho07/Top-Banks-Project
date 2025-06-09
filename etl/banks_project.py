import requests, pandas as pd, sqlite3
from bs4 import BeautifulSoup
from etl.help_extract_top_banks import populate_top_banks_df
from etl.help_transform_top_banks import convert_usd
from etl.log_progress import log_progress
from sqlite_connection_manager.sqlite_connection_manager import SqliteConnectionManager


data_url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
exchange_rates_path = "./data/exchange_rate.csv"
table_name = "Largest_banks"
top_banks_df = pd.DataFrame(
    columns=[
        "Rank",
        "Bank_name",
        "Market_cap_(USD_Billion)",
    ]
)


def execute_using_sql_connection(operation, *args):
    with SqliteConnectionManager() as sql_connection:
        return operation(sql_connection, *args)


def extract(data_url, top_banks_df):
    html_page = requests.get(data_url).text
    html_data = BeautifulSoup(html_page, "html.parser")
    html_tables = html_data.find_all("tbody")
    html_rows = html_tables[0].find_all("tr")
    log_progress("Preliminaries complete. Initiating ETL process")
    return populate_top_banks_df(html_rows, top_banks_df)


def transform(top_banks_df, csv_path):

    top_banks_df = convert_usd(top_banks_df, "Market_cap_(USD_Billion)", csv_path)

    print(top_banks_df)
    log_progress("Data transformation complete. Initiating Loading process")
    return top_banks_df


def load_to_csv(transformed_df, output_path):
    transformed_df.to_csv(output_path)
    log_progress("Data saved to CSV file")


def load_to_db(sql_connection, top_banks_df, table_name):
    top_banks_df.to_sql(table_name, sql_connection, if_exists="replace")
    log_progress("Data loaded to Database as a table, Executing queries")


def run_query(sql_connection, query_statement):
    cursor = sql_connection.cursor()

    cursor.execute(query_statement)
    print(cursor.fetchall())
    log_progress("Process Complete")


top_banks_df = extract(data_url, top_banks_df)
top_banks_df = transform(top_banks_df, exchange_rates_path)

load_to_csv(top_banks_df, "./output_data/largest_banks_data.csv")


execute_using_sql_connection(load_to_db, top_banks_df, table_name)
execute_using_sql_connection(run_query, "SELECT * FROM Largest_banks")
execute_using_sql_connection(run_query, "SELECT AVG(MC_GBP_Billion) FROM Largest_banks")
execute_using_sql_connection(run_query, "SELECT Bank_name FROM Largest_banks LIMIT 5")
