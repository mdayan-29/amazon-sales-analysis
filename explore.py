import pandas as pd
# Load the pandas library so we can work with tables of data (DataFrames)

df = pd.read_csv("Amazon Sale Report.csv", low_memory=False)
# Read the CSV into a table called df; low_memory=False avoids type-guessing issues

print(df.shape)
# Show (rows, columns) — confirms the file loaded fully

print(df.columns.tolist())
# List every column name

print(df.head())
# Show the first 5 rows to preview the data

print(df.isnull().sum())
# Count missing values in every column

print(df[df["Amount"].isnull()]["Status"].value_counts())
# For rows where Amount is missing, show which Status they have most often
# (used to check if missing Amount = mostly cancelled orders)

df_clean = df[df["Amount"].notnull()]
# Create a new table, keeping only rows where Amount has a value

print(df_clean.shape)
# Confirm how many rows remain after filtering

df_clean = df_clean.drop(columns=["Unnamed: 22"])
# Remove the "Unnamed: 22" column — mostly empty, not useful

df_clean["Date"] = pd.to_datetime(df_clean["Date"])
# Convert Date from text into a real date type for time-based analysis

print(df_clean.dtypes)
# Confirm Date is now a proper datetime type

'''Cleaning par is done now, let's head to analysis now''' 

df_clean.to_csv("cleaned_data.csv", index=False)
