# pip install alpha_vantage
from alpha_vantage.timeseries import TimeSeries

key = '20NKEQN455YWFM4T'
ts = TimeSeries(key)
aapl = ts.get_intraday(symbol='AAPL')
print(aapl)
