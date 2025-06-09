import csv, numpy as np, pandas as pd


def get_exchange_rates(csv_path):
    exchange_rates = {}

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            exchange_rates[row["Currency"]] = float(row["Rate"])

    return exchange_rates


def create_new_column_names(df_column_name):
    currency_billion_list = [
        "MC_GBP_Billion",
        "MC_EUR_Billion",
        "MC_INR_Billion",
    ]
    return [
        df_column_name.replace("Market_cap_(USD_Billion)", currency_billion)
        for currency_billion in currency_billion_list
    ]


def convert_usd(top_banks_df, df_column_name, csv_path):
    usd_column = pd.to_numeric(top_banks_df[df_column_name])

    for name in create_new_column_names(df_column_name):
        for currency, currency_conversion_unit in get_exchange_rates(csv_path).items():
            if currency in name:
                top_banks_df[name] = usd_column.apply(
                    lambda market_cap_value: (
                        np.round(market_cap_value * currency_conversion_unit, 2)
                    )
                )

    return top_banks_df
