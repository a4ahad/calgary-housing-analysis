import pandas as pd

# Load the file
# Replace the filename if your terminal shows a different exact name
filename = 'Census_by_Community_2019_20260608.csv' 

try:
    df = pd.read_csv(filename)
    
    # Display the first 5 rows
    print("--- First 5 rows of your data ---")
    print(df.head())
    
    # Display the columns
    print("\n--- Available Columns ---")
    print(df.columns.tolist())
    
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Make sure it is in the same folder as this script.")