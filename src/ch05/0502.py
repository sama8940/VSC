#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

print("pandas version: ", pd.__version__)


file_path = 'sample.csv'

# ファイルパスを指定してCSVファイルを読み込む
df = pd.read_csv(file_path)

print("head: ", df.head())

#     id  name  age
# 0   1  John   22

# データを1行ずつ取得
for index, row in df.iterrows():
    print("index: ", index)
    print(" row['id']: ", row['id'])
    print(" row['name']: ", row['name'])
    print(" row['age']: ", row['age'])

