import pandas as pd
import sqlite3
import os

# Path to the folder on the desktop
folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'Election Results')

# List all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('loksabha_elections.db')

# Loop through each file
for file in excel_files:
    file_path = os.path.join(folder_path, file)
    # Read each sheet in the Excel file
    excel_data = pd.read_excel(file_path, sheet_name=None)
    for sheet_name, df in excel_data.items():
        # Save each sheet to a table in the SQLite database
        df.to_sql(sheet_name, conn, if_exists='replace', index=False)

# Close the connection
conn.close()
