from etl.log_progress import log_progress


def run_query(sql_connection, query_statement):
    cursor = sql_connection.cursor()

    cursor.execute(query_statement)
    log_progress("Process Complete")
    return cursor.fetchall()
