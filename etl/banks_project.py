import requests, sqlite3, pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

data_url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"


def log_progress(message):
    time_format = "%Y-%h-%d-%H:%M:%S"
    current_date = datetime.now()
    time_stamp = current_date.strftime(time_format)

    with open("code_log", "a") as log_file:
        log_file.write(time_stamp + "," + message + "\n")
