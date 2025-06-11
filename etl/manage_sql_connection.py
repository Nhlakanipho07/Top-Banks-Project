from sqlite_connection_manager.sqlite_connection_manager import SqliteConnectionManager


def execute_using_sql_connection(operation, *args):
    with SqliteConnectionManager() as sql_connection:
        return operation(sql_connection, *args)
