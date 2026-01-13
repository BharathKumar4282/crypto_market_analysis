import pandas as pd
import requests
from sqlalchemy import create_engine 
from sqlalchemy import text

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency" : "usd",
    "order" : "market_cap_desc",
    "per_page" : 50,
    "page" : 1,
    "sparkline":False
}

response = requests.get(url,params=params)
data = response.json()
df = pd.DataFrame(data)

# DATA CLEANING

df = df.dropna(subset=['current_price','market_cap'])
df['last_updated'] = pd.to_datetime(df["last_updated"])

df['price_change_ratio'] = df["price_change_percentage_24h"] / 100
df['volatility_index'] = (df['high_24h'] - df['low_24h']) / df['current_price']

df_sql = df[[
    'id',
    'symbol',
    'name',
    'current_price',
    'market_cap',
    'total_volume',
    'price_change_percentage_24h',
    'last_updated'
]]

# LOAD INTO SQL
engine = create_engine(
       "mysql+pymysql://root:bharath_123@localhost:3306/crypto_db"
)

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT DATABASE();"))
#     print("Connected to:", result.fetchone())

df_sql.to_sql(name='crypto_table',con=engine,if_exists='append',index=False)

# print(df_sql.shape)
# print(df_sql.head())

import seaborn as sns
import matplotlib.pyplot as plt

query = "SELECT current_price, market_cap FROM crypto_table;"
df_analysis = pd.read_sql(query, con=engine)

sns.scatterplot(data=df_analysis, x='market_cap', y='current_price')
plt.show()
