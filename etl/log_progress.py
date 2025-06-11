from datetime import datetime


def log_progress(message):
    time_format = "%Y-%h-%d-%H:%M:%S"
    current_date = datetime.now()
    time_stamp = current_date.strftime(time_format)

    with open("../logs/code_log", "a") as log_file:
        log_file.write(f"""{time_stamp} : {message}\n""")
