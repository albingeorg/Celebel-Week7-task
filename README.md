# Data Lake ETL Pipeline

This ETL pipeline processes 3 different types of CSV files stored in a data lake. Each file is processed according to its type, and data is loaded into the appropriate database table using a truncate-and-load strategy.

## File Types & Processing Logic

### 1. CUST_MSTR_YYYYMMDD.csv
- Adds a column `load_date` extracted from the filename (format: YYYY-MM-DD).
- Loaded into the `CUST_MSTR` table.

### 2. master_child_export-YYYYMMDD.csv
- Adds columns `load_date` (YYYY-MM-DD) and `date_key` (YYYYMMDD).
- Loaded into the `master_child` table.

### 3. H_ECOM_ORDER.csv
- Loaded as-is into the `H_ECOM_Orders` table.

## Files

- `process_cust_mstr.py` — Logic to handle CUST_MSTR files.
- `process_master_child.py` — Logic to handle master_child_export files.
- `process_ecom_order.py` — Logic to handle H_ECOM_ORDER files.
- `run_daily_etl.py` — Entry point to loop over all files and apply appropriate logic.
- `README.md` — This documentation.

## Usage

1. Place your CSV files in a directory (e.g., `/raw/`).
2. Update `connection` in `run_daily_etl.py` with your database connection.
3. Call `run_daily_etl('/path/to/data', connection)` to process all files.

Ensure all files for the day are present before running the script.
