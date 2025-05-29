import pandas as pd
from etl.extract_top_banks import extract
from etl.transform_table_df import transform


pd.set_option("display.max_columns", None)

table_df = pd.DataFrame(
    columns=[
        "Bank_name",
        "Global_Data_Rank",
        "Global_Data_Market_cap_(USD_Billion)",
        "Forbes_India_Rank",
        "Forbes_India_Market_cap_(USD_Billion)",
    ]
)

global_data_heading = "Global_Data_Market_cap_"
forbes_india_heading = "Forbes_India_Market_cap_"
market_cap_dict = {
    global_data_heading + "(GBP Billion)": [],
    forbes_india_heading + "(GBP Bilion)": [],
    global_data_heading + "(EUR Billion)": [],
    forbes_india_heading + "(EUR Billion)": [],
    global_data_heading + "(INR Billion)": [],
    forbes_india_heading + "(INR Billion)": [],
}

table_df = extract(table_df)
table_df = transform(table_df, market_cap_dict)

print(table_df)
