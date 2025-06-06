import pandas as pd


def load_to_csv(transformed_data, target_file):
    transformed_data.to_csv(target_file)
