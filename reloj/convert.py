import pandas as pd

# Hearthrate
df = pd.read_csv('input/hearthrate-auto.csv')
df.date = pd.to_datetime(df.date)
df.date = pd.to_datetime(df.date)
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df.to_parquet('reloj-data/hearthrate-auto', partition_cols=['year', 'month'])

# Sleep
df = pd.read_csv('input/sleep.csv')
df.date = pd.to_datetime(df.date)
df.date = pd.to_datetime(df.date)
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df.to_parquet('reloj-data/sleep', partition_cols=['year', 'month'])
