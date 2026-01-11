__version__ = "1.0.0"
__author__ = "Emanuele Tarchi"

import pandas as pd
import os

def clean_csv(input_file, output_file="cleaned_data.csv"):
    """
    Automated CSV cleaning script: removes empty rows, trims whitespace, 
    and normalizes data types.
    """
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' was not found.")
        return

    print(f"Reading {input_file}...")
    df = pd.read_csv(input_file)

    # Remove rows that are completely empty
    df.dropna(how="all", inplace=True)

    # Trim leading/trailing whitespace from strings
    # Note: .applymap is replaced by .map in newer pandas versions for element-wise operations
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    # Convert columns to numeric where possible, ignoring errors for text columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="ignore")

    # Save the cleaned file
    df.to_csv(output_file, index=False)
    print(f"Success! Cleaned file saved as: {output_file}")

if __name__ == "__main__":
    # Example usage: Replace 'sample.csv' with your actual file path
    clean_csv("sample.csv")
