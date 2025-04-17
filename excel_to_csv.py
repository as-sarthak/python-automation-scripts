import pandas as pd
import os

folder_path = 'your_excel_folder_here'

for file in os.listdir(folder_path):
    if file.endswith('.xlsx') or file.endswith('.xls'):
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        csv_file = os.path.splitext(file)[0] + '.csv'
        df.to_csv(os.path.join(folder_path, csv_file), index=False)

print("Excel files converted to CSV!")
