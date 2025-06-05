import pandas as pd
from etl.extract_top_banks import extract
from etl.transform_table_df import transform


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

print(top_banks_df)
