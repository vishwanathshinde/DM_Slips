import pandas as pd
import matplotlib.pyplot as plt
stock_market={'Year':[2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016,2016],
                'Month':[12,11,10,9,8,7,6,5,4,3,2,1,12,11,10,9,8,7,6,5,4,3,2,1],
                'Interest_rate':[2.75,2.5,2.5,2.5,2.5,2.5,2.5,2.25,2.25,2.25,2,2,2,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75,1.75],
                'unemployement_rate':[5.3,5.3,5.3,5.3,5.4,5.6,5.5,5.5,5.5,5.6,5.7,5.9,6,5.9,5.8,6.1,6.2,6.1,6.1,6.1,5.9,6.2,6.2,6.1],
                'stock_index_price':[1464,1394,1357,1293,1256,1254,1234,1195,1159,1167,1130,1075,1047,965,943,958,971,949,884,866,876,822,704,719]}

df=pd.DataFrame(stock_market,columns=['Year','Month','Interest_rate','unemployement_rate','stock_index_price'])
plt.scatter(df['Interest_rate'],df['stock_index_price'],color='red')
# <matplotlib.collections.PathCollection object at 0x00000167E14EB990>
plt.title('stock index price vs Interest rate',fontsize=14)
# Text(0.5, 1.0, 'stock index price vs Interest rate')
plt.xlabel('Interest Rate',fontsize=14)
# Text(0.5, 0, 'Interest Rate')
plt.ylabel('Stock Index price',fontsize=14)
# Text(0, 0.5, 'Stock Index price')
plt.grid(True)
plt.show()
