import pandas as pd

{
    "Global_Data_Market_cap_(GBP Billion)": None,
    "Forbes_India_Market_cap_(GBP Bilion)": None,
    "Global_Data_Market_cap_(EUR Billion)": None,
    "Forbes_India_Market_cap_(EUR Billion)": None,
    "Global_Data_Market_cap_(INR Billion)": None,
    "Forbes_India_Market_cap_(INR Billion)": None,
    "Global_Data_Market_cap_(USD_Billion)": "",
    "Forbes_India_Market_cap_(USD_Billion)": "169.17",
}

exchange_rates = {
    "GBP": [0.8, 1, 2, 3],
    "EUR": [0.93, 5, 8, 7],
    "INR": [82.95, 8, 7, 9],
}

df = pd.DataFrame(exchange_rates, index=[0, 1, 2, 3])

print(df)

df["G"] = df["GBP"].apply(lambda x: x * 2)

print(df)
