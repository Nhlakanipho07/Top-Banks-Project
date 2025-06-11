import sqlite3
from logs.log_progress import log_progress


class SqliteConnectionManager:
    def __init__(self):
        self.db_name = "../banks_database/Banks.db"
        self.sql_connection = None

    def __enter__(self):
        self.sql_connection = sqlite3.connect(self.db_name)
        log_progress("SQL Connection initiated")
        return self.sql_connection

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is None:
            self.sql_connection.commit()
        else:
            self.sql_connection.rollback()
        self.sql_connection.close()
        log_progress("Server Connection closed")
