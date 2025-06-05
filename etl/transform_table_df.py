import pandas as pd


def convert_usd(top_banks_df, df_column_name):
    new_column_names = []
    usd_column = top_banks_df[df_column_name]

    currency_billion_list = [
        "(GBP_Billion)",
        "(EUR_Billion)",
        "(INR_Billion)",
    ]

    exchange_rates = {
        "GBP": 0.8,
        "EUR": 0.93,
        "INR": 82.95,
    }

    for currency_billion in currency_billion_list:
        new_column_names.append(
            df_column_name.replace("(USD_Billion)", currency_billion)
        )

    for new_column in new_column_names:
        for currency, conversion_unit in exchange_rates.items():
            if currency in new_column:
                top_banks_df[new_column] = usd_column.apply(
                    lambda market_cap: (
                        round(float(market_cap) * conversion_unit)
                        if market_cap.isdigit()
                        else market_cap
                    )
                )
            break
        # print(top_banks_df[new_column])

    return top_banks_df


def transform(top_banks_df):

    for df_column_name in [
        "Global_Data_Market_cap_(USD_Billion)",
        "Forbes_India_Market_cap_(USD_Billion)",
    ]:
        top_banks_df = convert_usd(top_banks_df, df_column_name)

    return top_banks_df
