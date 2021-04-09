import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("avocado.csv")
df.head()


#рабочий круговой график органических и химических авокадо
con_df = df.loc[df["type"] == "conventional"]
con_num = con_df.shape[0]
con_percent = con_num / df.shape[0] * 100
con_df.head()
org_df = df.loc[df["type"] == "organic"]
org_num = org_df.shape[0]
org_percent = org_num / df.shape[0] * 100
org_df.head()
type_pie = pd.DataFrame({'type': ['organic', 'conventional'],
                   'amount': [con_num, org_num]})
type_pie.set_index('type', inplace=True)

plot = type_pie.plot.pie(y='amount', figsize=(7, 7))
plt.show()


#рабочий график продаж за 2015 год по номерам авокад - столбчатая
df4046 = df.loc[df['year'] == 2015, '4046'].sum()
df4225 = df.loc[df['year'] == 2015, '4225'].sum()
df4770 = df.loc[df['year'] == 2015, '4770'].sum()
num_df = [df4046, df4225, df4770]
plt.title('Amount of every type of avocado in 2015', fontsize=15)
index = np.arange(3)
plt.bar(index, num_df)
plt.xticks(index+0.4,['4046','4225','4770'])
plt.show()

#круговая сколько авокад в каждом году продано
#надо выкинуть 2018
sum2015 = df.loc[df['year'] == 2015, 'Total Volume'].sum()
sum2016 = df.loc[df['year'] == 2016, 'Total Volume'].sum()
sum2017 = df.loc[df['year'] == 2017, 'Total Volume'].sum()
sum2018 = df.loc[df['year'] == 2018, 'Total Volume'].sum()
type_pie = pd.DataFrame({'year': ['2015', '2016', '2017', '2018'],
                   'amount': [sum2015, sum2016, sum2017, sum2018]})
type_pie.set_index('year', inplace=True)

plot = type_pie.plot.pie(y='amount', figsize=(7, 7))
plt.show()

#сколько в целом авокад было продано в каждом году кроме 2018 линейная
sum2015 = df.loc[df['year'] == 2015, 'Total Volume'].sum()
sum2016 = df.loc[df['year'] == 2016, 'Total Volume'].sum()
sum2017 = df.loc[df['year'] == 2017, 'Total Volume'].sum()
all_sum = [sum2015, sum2016, sum2017]
plt.title('Total avocado volume each year', fontsize=15)
plt.plot((2015, 2016, 2017), all_sum)
plt.xticks([2015, 2016, 2017])
plt.show()

#маленькие и большие упаковки - круговая
small_sum = df['Small Bags'].sum()
large_sum = df['Large Bags'].sum()
xlarge_sum = df['XLarge Bags'].sum()
type_pie = pd.DataFrame({'type': ['small', 'large', 'xlarge'],
                   'amount': [small_sum, large_sum, xlarge_sum]})
type_pie.set_index('type', inplace=True)

plot = type_pie.plot.pie(y='amount', figsize=(7, 7))
plt.show()


#как растет цена от каждого года - линейная

price2015 = df.loc[df['year'] == 2015, 'AveragePrice'].mean()
price2016 = df.loc[df['year'] == 2016, 'AveragePrice'].mean()
price2017 = df.loc[df['year'] == 2017, 'AveragePrice'].mean()
all_sum = [price2015, price2016, price2017]
plt.title('Average price every year', fontsize=15)
plt.plot((2015, 2016, 2017), all_sum)
plt.xticks([2015, 2016, 2017])
plt.show()

#количество покупок от региона - столбчатая
print (df['region'].value_counts())
#видим, что данные собирались с каждого региона и их слишком много, поэтому возьмем самые крпные
Detroit = df.loc[df['region'] == 'Detroit', 'Total Volume'].sum()
Philadelphia = df.loc[df['region'] == 'Philadelphia', 'Total Volume'].sum()
LosAngeles = df.loc[df['region'] == 'LosAngeles', 'Total Volume'].sum()
Houston = df.loc[df['region'] == 'Houston', 'Total Volume'].sum()
NewYork = df.loc[df['region'] == 'NewYork', 'Total Volume'].sum()
Chicago = df.loc[df['region'] == 'Chicago', 'Total Volume'].sum()
California = df.loc[df['region'] == 'California', 'Total Volume'].sum()
num_df = [Detroit, Philadelphia, LosAngeles, Houston, NewYork,
          Chicago, California]
plt.title('Amount of sales in regions', fontsize=15)

index = np.arange(7)
plt.bar(index, num_df)
plt.xticks(index, ['Detroit', 'Philadelphia', 'LosAngeles', 'Houston', 'NewYork',
          'Chicago', 'California'])
plt.show()


#покупки упаковок от года - линейная

price2015 = df.loc[df['year'] == 2015, 'Total Bags'].sum()
price2016 = df.loc[df['year'] == 2016, 'Total Bags'].sum()
price2017 = df.loc[df['year'] == 2017, 'Total Bags'].sum()
all_sum = [price2015, price2016, price2017]
plt.title('Amount of bags every year', fontsize=15)
plt.plot((2015, 2016, 2017), all_sum)
plt.xticks([2015, 2016, 2017])
plt.show()

#цена от региона - столбчатая
Detroit = df.loc[df['region'] == 'Detroit', 'AveragePrice'].mean()
Philadelphia = df.loc[df['region'] == 'Philadelphia', 'AveragePrice'].mean()
LosAngeles = df.loc[df['region'] == 'LosAngeles', 'AveragePrice'].mean()
Houston = df.loc[df['region'] == 'Houston', 'AveragePrice'].mean()
NewYork = df.loc[df['region'] == 'NewYork', 'AveragePrice'].mean()
Chicago = df.loc[df['region'] == 'Chicago', 'AveragePrice'].mean()
California = df.loc[df['region'] == 'California', 'AveragePrice'].mean()
num_df = [Detroit, Philadelphia, LosAngeles, Houston, NewYork,
          Chicago, California]
plt.title('Average price every region', fontsize=15)
index = np.arange(7)
plt.bar(index, num_df)
plt.xticks(index, ['Detroit', 'Philadelphia', 'LosAngeles', 'Houston', 'NewYork',
          'Chicago', 'California'])
plt.show()


#продажи по номерам за все годы - линейная
df4046 = df.loc[df['year'] == 2015, '4046'].sum()
df4225 = df.loc[df['year'] == 2016, '4046'].sum()
df4770 = df.loc[df['year'] == 2017, '4046'].sum()
num_df4046 = [df4046, df4225, df4770]
df4046 = df.loc[df['year'] == 2015, '4225'].sum()
df4225 = df.loc[df['year'] == 2016, '4225'].sum()
df4770 = df.loc[df['year'] == 2017, '4225'].sum()
num_df4225 = [df4046, df4225, df4770]
df4046 = df.loc[df['year'] == 2015, '4770'].sum()
df4225 = df.loc[df['year'] == 2016, '4770'].sum()
df4770 = df.loc[df['year'] == 2017, '4770'].sum()
num_df4770 = [df4046, df4225, df4770]
print(num_df4046)
print(num_df4225)
print(num_df4770)
plt.title('Amount of every type of avocado', fontsize=15)
plt.plot([2015, 2016, 2017], num_df4046, label="4046")
plt.plot([2015, 2016, 2017], num_df4225, label="4225")
plt.plot([2015, 2016, 2017], num_df4770, label="4770")
plt.xticks([2015, 2016, 2017])
plt.legend()
plt.show()
