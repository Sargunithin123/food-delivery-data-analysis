import pandas as pd
import sqlite3
import json

# Load orders.csv
df_orders = pd.read_csv('data/orders.csv')

# Load users.json
with open('data/users.json', 'r') as f:
    users_data = json.load(f)
df_users = pd.DataFrame(users_data)

# Load restaurants.sql into a DataFrame
conn = sqlite3.connect(':memory:')
with open('data/restaurants.sql', 'r') as f:
    sql_script = f.read()
conn.executescript(sql_script)
df_restaurants = pd.read_sql_query('SELECT * FROM restaurants', conn)
conn.close()

# Merge orders with users on user_id
df_merged = pd.merge(df_orders, df_users, on='user_id', how='left')

# Merge with restaurants on restaurant_id
df_final = pd.merge(df_merged, df_restaurants, on='restaurant_id', how='left')

# Save to CSV
df_final.to_csv('output/final_food_delivery_dataset.csv', index=False)

print("Data merged and saved to output/final_food_delivery_dataset.csv")
