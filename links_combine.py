import pandas as pd
import glob
import os

# Path to the folder containing your Excel files
folder_path = '年报链接-固态电池-2024'   # <-- CHANGE THIS

# Get all Excel files in the folder (modify the extension if needed)
file_list = glob.glob(os.path.join(folder_path, '*.xlsx'))

# List to hold individual DataFrames
df_list = []

for file in file_list:
    df = pd.read_excel(file)
    df_list.append(df)

    if len(df) == 0:
        print(file)


# Concatenate all DataFrames
combined_df = pd.concat(df_list, ignore_index=True)

# Save to a new Excel file
combined_df.to_excel(folder_path+'/links_combined.xlsx', index=False)   # Save as Excel
# Or save as CSV:
# combined_df.to_csv('combined.csv', index=False)
