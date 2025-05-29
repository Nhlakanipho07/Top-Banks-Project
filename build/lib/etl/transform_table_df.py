import pandas as pd


def fill_market_cap(
    market_cap_dict, market_cap_key, eur_conversion, gbp_conversion, inr_conversion
):
    if "EUR" in market_cap_key:
        market_cap_dict[market_cap_key] = eur_conversion
    elif "GBP" in market_cap_key:
        market_cap_dict[market_cap_key] = gbp_conversion
    elif "INR" in market_cap_key:
        market_cap_dict[market_cap_key] = inr_conversion


def perform_conversion(table_df, market_cap_dict, column_heading):
    eur_conversion = None
    gbp_conversion = None
    inr_conversion = None

    for capital in table_df[column_heading]:
        if capital.isdigit():
            capital = float(capital)
            eur_conversion = round(capital * 0.93, 2)
            gbp_conversion = round(capital * 0.8, 2)
            inr_conversion = round(capital * 82.95, 2)
        else:
            market_cap_dict[column_heading] = capital

    for index, market_cap_key in enumerate(list(market_cap_dict.keys())):
        if "Global" in column_heading:
            if index % 2 != 0:
                fill_market_cap(
                    market_cap_dict,
                    market_cap_key,
                    eur_conversion,
                    gbp_conversion,
                    inr_conversion,
                )
        elif "Forbes" in column_heading:
            if index % 2 == 0:
                fill_market_cap(
                    market_cap_dict,
                    market_cap_key,
                    eur_conversion,
                    gbp_conversion,
                    inr_conversion,
                )


def populate_market_cap(table_df, market_cap_dict):
    perform_conversion(
        table_df, market_cap_dict, "Global_Data_Market_cap_(USD_Billion)"
    )
    perform_conversion(
        table_df, market_cap_dict, "Forbes_India_Market_cap_(USD_Billion)"
    )

    return market_cap_dict


def transform(table_df, market_cap_dict):
    x = populate_market_cap(table_df, market_cap_dict)
    print(x)


#     table_df[list(market_cap_dict.keys())] = pd.DataFrame(
#         populate_market_cap(table_df, market_cap_dict)
#     )
#     return table_df
