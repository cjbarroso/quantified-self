import pandas as pd

#TODO: Usar otro separador porque el engine python es mas lento que el default C, pero n puedo usarlo por el separador de mas de un caracter
df = pd.read_csv('input/activity-watcher.csv', sep='ء', engine='python')
df.starttime = pd.to_datetime(df.starttime)
df.endtime = pd.to_datetime(df.endtime)

# Evitar errores de precision raros
df['starttime'] = df['starttime'].astype('datetime64[ms]')
df['endtime'] = df['endtime'].astype('datetime64[ms]')

df['year'] = df['starttime'].dt.year
df['month'] = df['starttime'].dt.month
df['day'] = df['starttime'].dt.day

df.to_parquet('activity-watcher-events', partition_cols=['year', 'month', 'day'] )
