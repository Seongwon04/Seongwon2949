import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('C:\GDP Trend_OECD.csv')


filtered_data = data[data['Country'] == 'USA'] #USA 데이터만 쓰기
X = filtered_data.loc[:,'Year'] #X축을 Year로 지정
Y = filtered_data.loc[:,'GDP'] #Y축을 GDP로 지정

X = X.sort_values()
Y = Y.sort_values()

plt.xlabel('Year')
plt.ylabel('GDP')
plt.plot(X,Y)
plt.show()




