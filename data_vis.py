import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('db.sqlite')

df = pd.read_sql('select * from prices', conn)
df['date'] = pd.to_datetime(df['date'])
df2 = df.set_index('date')

chart = df2.plot()
print(chart)
plt.show()