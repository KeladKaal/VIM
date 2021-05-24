
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from wordcloud import WordCloud
df = pd.read_csv("avocado.csv")
df.head()

seasons = {'Winter': (1, 2, 12),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

abc=[]
for i in range (18249):
    month = str(df["Date"][i][5])+str(df["Date"][i][6])
    for key in seasons.keys():
        if int(month) in seasons[key]:
            abc.append(key)


df.sort_values(by='Date')
#print(str(df["Date"][7][5])+str(df["Date"][7][6]))


#продажи авокадо в каждом году
fig = px.line(df, y="Total Volume", x="Date", title="Sales of avocado each year")
fig.show()



#регионы где продается авокадо
text = " ".join(df["region"].tolist())
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False).generate(text)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()



#количество авокадо от сезона
winter = 0
spring = 0
summer = 0
autumn = 0
for i in range (18249):
    if abc[i]=="Winter":
        winter += df["Total Volume"][i]
    if abc[i]=="Spring":
        spring += df["Total Volume"][i]
    if abc[i]=="Summer":
        summer += df["Total Volume"][i]
    if abc[i]=="Autumn":
        autumn += df["Total Volume"][i]
values = [winter, spring, summer, autumn]
fig = px.pie(labels=["Winter", "Spring", "Summer", "Autumn"], title="Sales of avocado each season", values=values, names=["Winter", "Spring", "Summer", "Autumn"], hole=.5)
fig.show()



#цена авокадо от сезона
winter = 0
spring = 0
summer = 0
autumn = 0
for i in range (18249):
    if abc[i]=="Winter":
        winter += df["AveragePrice"][i]
    if abc[i]=="Spring":
        spring += df["AveragePrice"][i]
    if abc[i]=="Summer":
        summer += df["AveragePrice"][i]
    if abc[i]=="Autumn":
        autumn += df["AveragePrice"][i]
values = [winter, spring, summer, autumn]
fig = px.pie(labels=["Winter", "Spring", "Summer", "Autumn"], title="Price of avocado every season", values=values, names=["Winter", "Spring", "Summer", "Autumn"], hole=.5)
fig.show()



#цена в августе
lst = []
data = []
for i in range (18249):
    month = str(df["Date"][i][5]) + str(df["Date"][i][6])
    year = str(df["Date"][i][3])
    if (month == "08") and (year == "5"):
        lst.append(df["AveragePrice"][i])
        data.append(df["Date"][i])
fig = px.scatter( y=lst, x=data, title="Price of avocado in august")
fig.show()


#продажи за август
lst = []
data = []
for i in range (18249):
    month = str(df["Date"][i][5]) + str(df["Date"][i][6])
    year = str(df["Date"][i][3])
    if (month == "08") and (year == "5"):
        lst.append(df["Total Volume"][i])
        data.append(df["Date"][i])
fig = px.scatter( y=lst, x=data, title="Sales of avocado in august")
fig.show()



#количество упаковок от сезона

winter = 0
spring = 0
summer = 0
autumn = 0
for i in range (18249):
    if abc[i]=="Winter":
        winter += df["Total Bags"][i]
    if abc[i]=="Spring":
        spring += df["Total Bags"][i]
    if abc[i]=="Summer":
        summer += df["Total Bags"][i]
    if abc[i]=="Autumn":
        autumn += df["Total Bags"][i]
values = [winter, spring, summer, autumn]
fig = px.pie(labels=["Winter", "Spring", "Summer", "Autumn"], title="Sales of avocado bags every season", values=values, names=["Winter", "Spring", "Summer", "Autumn"], hole=.5)
fig.show()