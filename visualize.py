import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('calgary.db')
df = pd.read_sql_query("SELECT NAME, (RES_CNT * 1.0 / DWELL_CNT) as density FROM communities ORDER BY density DESC LIMIT 10", conn)

# Create a simple bar chart
plt.figure(figsize=(10,6))
plt.bar(df['NAME'], df['density'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Calgary Communities by Resident-to-Dwelling Density')
plt.ylabel('Residents per Dwelling')
plt.tight_layout()

# Save the plot as an image
plt.savefig('density_chart.png')
print("Chart saved as density_chart.png!")