import pandas as pd
import math
from math import fsum
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np
df = pd.read_csv("avocado.csv")
df.head()

#проверка столбца Total Bags
df["check_sum"] = df["Small Bags"]+df["Large Bags"]+df["XLarge Bags"]

sum2015 = df.loc[df['year'] == 2015, 'check_sum'].sum()
sum2016 = df.loc[df['year'] == 2016, 'check_sum'].sum()
sum2017 = df.loc[df['year'] == 2017, 'check_sum'].sum()
all_sum = [sum2015, sum2016, sum2017]
sum2015 = df.loc[df['year'] == 2015, 'Total Bags'].sum()
sum2016 = df.loc[df['year'] == 2016, 'Total Bags'].sum()
sum2017 = df.loc[df['year'] == 2017, 'Total Bags'].sum()
all_summ = [sum2015, sum2016, sum2017]
plt.title('Total avocado volume each year', fontsize=15)
plt.plot((2015, 2016, 2017), all_summ)
plt.plot((2015, 2016, 2017), all_sum)
plt.xticks([2015, 2016, 2017])
plt.show()

#обработка типа авокадо
df_norm = df.copy()
df_norm["type"].unique()
def norm_type(letter: str) -> int:
  if letter == "conventional":
    return 0
  else:
    return 1

df_norm["type"] = df_norm["type"].apply(norm_type)
df_norm.head()
print(df_norm["type"].unique())


#обработка региона авокадо
reg_list = df_norm["region"].unique()
def norm_region(letter: str) -> int:
  for i in range(len(reg_list)):
      if letter == reg_list[i]:
          return i+1

df_norm["region"] = df_norm["region"].apply(norm_region)
df_norm.head()
print(df_norm["region"].unique())


#округление всех столбцов которым это надо
df_norm["4046"] = round(df_norm["4046"])
df_norm.head()
print(df_norm["4046"].unique())

df_norm["4225"] = round(df_norm["4225"])
df_norm.head()
print(df_norm["4225"].unique())

df_norm["4770"] = round(df_norm["4770"])
df_norm.head()
print(df_norm["4770"].unique())

df_norm["Total Bags"] = round(df_norm["Total Bags"])
df_norm.head()
print(df_norm["Total Bags"].unique())

df_norm["Small Bags"] = round(df_norm["Small Bags"])
df_norm.head()
print(df_norm["Small Bags"].unique())

df_norm["Large Bags"] = round(df_norm["Large Bags"])
df_norm.head()
print(df_norm["Large Bags"].unique())


print(df[df['AveragePrice'].isnull()])


