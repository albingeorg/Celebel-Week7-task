import pandas as pd
import re

def process_master_child(file_path, table_name, connection):
    match = re.search(r"master_child_export-(\d{8})\.csv", file_path)
    if match:
        date_str = match.group(1)
        formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
        df = pd.read_csv(file_path)
        df['load_date'] = formatted_date
        df['date_key'] = date_str
        connection.execute(f"TRUNCATE TABLE {table_name}")
        df.to_sql(table_name, connection, if_exists='append', index=False)
