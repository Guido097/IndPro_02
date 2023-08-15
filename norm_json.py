import pandas as pd
import numpy as np
import requests
import json
import ast
from pycoingecko import CoinGeckoAPI

df_bitcoin = pd.read_json(".json")


df_bitcoin["prices"] = df_bitcoin["prices"].astype(str)
df_bitcoin["market_caps"] = df_bitcoin["market_caps"].astype(str)
df_bitcoin["total_volumes"] = df_bitcoin["total_volumes"].astype(str)

df_bitcoin["unix_timestamp"] = df_bitcoin["prices"].apply(lambda x: int(x.split(", ")[0][1:]))
df_bitcoin["date"] = pd.to_datetime(df_bitcoin["unix_timestamp"], unit="ms")
df_bitcoin.head(10)

df_bitcoin["prices"] = df_bitcoin["prices"].apply(ast.literal_eval)
df_bitcoin["market_caps"] = df_bitcoin["market_caps"].apply(ast.literal_eval)
df_bitcoin["total_volumes"] = df_bitcoin["total_volumes"].apply(ast.literal_eval)

def remove_unix_timestamp(entry):
    return entry[1]

df_bitcoin["prices"] = df_bitcoin["prices"].apply(remove_unix_timestamp)
df_bitcoin["market_caps"] = df_bitcoin["market_caps"].apply(remove_unix_timestamp)
df_bitcoin["total_volumes"] = df_bitcoin["total_volumes"].apply(remove_unix_timestamp)

df_bitcoin = df_bitcoin.drop(columns=['unix_timestamp'])

pd.set_option('display.float_format', '{:.2f}'.format)
pd.options.display.float_format = '{:.15f}'.format
df_bitcoin['year'] = df_bitcoin['date'].dt.year
df_bitcoin.head(10)