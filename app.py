#%%
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as pdr
import yahoo_fin.stock_info as si
import numpy as np
import json 

start = datetime(2020, 3, 31)
end = datetime(2022, 12, 31)

FIRST_TICK = 'QQQ'
SECOND_TICK = 'ARKK'
print(FIRST_TICK)
print("-----------------------------------------------")
print(json.dumps(si.get_quote_table(FIRST_TICK),indent=4, sort_keys=True))
print(SECOND_TICK)
print("-----------------------------------------------")
print(json.dumps(si.get_quote_table(SECOND_TICK),indent=4, sort_keys=True))




stockOne = pdr.DataReader(FIRST_TICK, 'yahoo', start, end)

stockTwo = pdr.DataReader(SECOND_TICK, 'yahoo', start, end)

# plots out close price of a stock

stockOne_adj = np.array(stockOne['Close'])
stockTwo_adj = np.array(stockTwo['Close'])

corr_matrix = np.corrcoef(stockOne_adj, stockTwo_adj)
corr = corr_matrix[0,1]
R_sq = corr**2
print ("R = ",R_sq**0.5)
print("R2 = ",R_sq)


plt.figure(dpi=400)



stockOne['Adj Close'].plot(legend=True, figsize=(15, 15), label = FIRST_TICK)

stockTwo['Adj Close'].plot(legend=True, figsize=(15, 15), label = SECOND_TICK)





# print(corr_matrix)



# %%
