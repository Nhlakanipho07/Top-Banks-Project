import pandas as pd
import sqlite3
from etl.extract_top_banks import extract
from etl.transform_top_banks import transform
from etl.load_top_banks import load_to_csv


db_name = "Banks.db"
table_name = "Largest_banks"
pd.set_option("display.max_columns", None)

top_banks_df = pd.DataFrame(
    columns=[
        "Bank_name",
        "Global_Data_Rank",
        "Global_Data_Market_cap_(USD_Billion)",
        "Forbes_India_Rank",
        "Forbes_India_Market_cap_(USD_Billion)",
    ]
)


top_banks_df = extract(top_banks_df)
top_banks_df = transform(top_banks_df)
# load_to_csv(top_banks_df, "output_data/largest_banks_data.csv")


conn = sqlite3.connect(db_name)
top_banks_df.to_sql(table_name, conn, if_exists="replace", index=False)
conn.close()
