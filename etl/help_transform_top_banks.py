import csv, numpy as np, pandas as pd
from etl.log_progress import log_progress


def get_exchange_rates(csv_path):
    exchange_rates = {}

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            exchange_rates[row["Currency"]] = float(row["Rate"])
    return exchange_rates


def convert_usd(top_banks_df, df_column_name, csv_path):
    exchange_rates = get_exchange_rates(csv_path)

    for name in [
        "MC_GBP_Billion",
        "MC_EUR_Billion",
        "MC_INR_Billion",
    ]:
        for currency, currency_conversion_unit in exchange_rates.items():
            if currency in name:
                top_banks_df[name] = top_banks_df[df_column_name].apply(
                    lambda market_cap_value: (
                        np.round(market_cap_value * currency_conversion_unit, 2)
                    )
                )
    return top_banks_df


def transform(top_banks_df, csv_path):
    top_banks_df = convert_usd(top_banks_df, "Market_cap_(USD_Billion)", csv_path)
    print(top_banks_df)
    log_progress("Data transformation complete. Initiating Loading process")
    return top_banks_df
