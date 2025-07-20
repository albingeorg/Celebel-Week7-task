import pandas as pd

def process_ecom_order(file_path, table_name, connection):
    df = pd.read_csv(file_path)
    connection.execute(f"TRUNCATE TABLE {table_name}")
    df.to_sql(table_name, connection, if_exists='append', index=False)
