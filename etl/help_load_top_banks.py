import pandas as pd
from etl.log_progress import log_progress


def load_to_csv(transformed_df, output_path):
    transformed_df.to_csv(output_path)
    log_progress("Data saved to CSV file")


def load_to_db(sql_connection, top_banks_df, table_name):
    top_banks_df.to_sql(table_name, sql_connection, if_exists="replace")
    log_progress("Data loaded to Database as a table, Executing queries")
