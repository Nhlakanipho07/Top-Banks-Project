import pandas as pd


def convert_usd(top_banks_df, df_column_name):
    currency_billion_list = [
        "(GBP_Billion)",
        "(EUR_Billion)",
        "(INR_Billion)",
    ]
    new_column_names = [
        df_column_name.replace("(USD_Billion)", currency_billion)
        for currency_billion in currency_billion_list
    ]
    exchange_rates = {
        "GBP": 0.8,
        "EUR": 0.93,
        "INR": 82.95,
    }
    usd_column = pd.to_numeric(top_banks_df[df_column_name])

    for name in new_column_names:
        for currency, conversion_unit in exchange_rates.items():
            if currency in name:
                top_banks_df[name] = usd_column.apply(
                    lambda market_cap: (round(market_cap * conversion_unit, 2))
                )

    return top_banks_df


def transform(top_banks_df):

    for df_column_name in [
        "Global_Data_Market_cap_(USD_Billion)",
        "Forbes_India_Market_cap_(USD_Billion)",
    ]:
        top_banks_df = convert_usd(top_banks_df, df_column_name)

    return top_banks_df
