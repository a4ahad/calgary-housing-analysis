import pandas as pd
import sqlite3

# 1. Load the data
df = pd.read_csv('Census_by_Community_2019_20260608.csv')

# 2. Connect to a local database (this creates 'calgary.db')
conn = sqlite3.connect('calgary.db')

# 3. Save the dataframe to a SQL table
df.to_sql('communities', conn, if_exists='replace', index=False)

# 4. Run a test query: Top 10 communities by population
# Change the query line to this:
query = """
SELECT NAME, RES_CNT, DWELL_CNT, 
       CAST(RES_CNT AS FLOAT) / CAST(DWELL_CNT AS FLOAT) as density_ratio
FROM communities 
ORDER BY RES_CNT DESC 
LIMIT 10;
"""

result = pd.read_sql_query(query, conn)
print("--- Top 10 Communities by Population ---")
print(result)

conn.close()