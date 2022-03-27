#%%
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as pdr
import numpy as np

start = datetime(2020, 3, 31)
end = datetime(2022, 12, 31)

FIRST_TICK = 'HMC'
SECOND_TICK = 'TSLA'

stockOne = pdr.DataReader(FIRST_TICK, 'yahoo', start, end)

stockTwo = pdr.DataReader(SECOND_TICK, 'yahoo', start, end)

# plots out close price of a stock

stockOne_adj = np.array(stockOne['Close'])
stockTwo_adj = np.array(stockTwo['Close'])

corr_matrix = np.corrcoef(stockOne_adj, stockTwo_adj)
corr = corr_matrix[0,1]
R_sq = corr**2
print(R_sq)


plt.figure(dpi=1200)

stockOne['Adj Close'].plot(legend=True, figsize=(15, 15), label = FIRST_TICK)

stockTwo['Adj Close'].plot(legend=True, figsize=(15, 15), label = SECOND_TICK)





# print(corr_matrix)



# %%
