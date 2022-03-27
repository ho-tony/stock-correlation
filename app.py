import datetime
import pandas as pd
import pandas_datareader.data as pdr
import numpy as np


date_from = datetime.date(2018, 1, 1)
date_to = datetime.date(2022, 12, 31)
tickerlist = ['AAPL']

data = pdr.DataReader(name="AAPL", data_source='yahoo', start=date_from, end= date_to)



print(data)
# print("hello world")