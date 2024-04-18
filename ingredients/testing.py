import pandas as pd

# Read the CSV file and display the first few rows
input_file = 'final.csv'

try:
    # Read the first few rows of the CSV file into a DataFrame
    df = pd.read_csv(input_file)
    
    # Display the first few rows
    print(df.head())

except FileNotFoundError:
    print("The file 'final.csv' does not exist in the specified location.")
