import os
from process_cust_mstr import process_cust_mstr
from process_master_child import process_master_child
from process_ecom_order import process_ecom_order

def run_daily_etl(data_dir, connection):
    for filename in os.listdir(data_dir):
        full_path = os.path.join(data_dir, filename)

        if filename.startswith("CUST_MSTR_") and filename.endswith(".csv"):
            process_cust_mstr(full_path, "CUST_MSTR", connection)
        elif filename.startswith("master_child_export-") and filename.endswith(".csv"):
            process_master_child(full_path, "master_child", connection)
        elif filename.startswith("H_ECOM_ORDER") and filename.endswith(".csv"):
            process_ecom_order(full_path, "H_ECOM_Orders", connection)
