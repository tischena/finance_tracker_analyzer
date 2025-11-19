"""
Loads transaction data from a local Excel file into a pandas DataFrame.

File Path:
    C:/Users/hp/Desktop/anas_transactions.xlsx

Returns:
    pandas.DataFrame: A DataFrame containing all loaded transaction data.
"""

import pandas as pd

# Load data from Excel file
df = pd.read_excel("C:/Users/hp/Desktop/anas_transactions.xlsx")