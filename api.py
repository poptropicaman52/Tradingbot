# pip install alpha_vantage
# https://github.com/RomelTorres/alpha_vantage
from alpha_vantage.timeseries import TimeSeries

key = '20NKEQN455YWFM4T'
ts = TimeSeries(key, output_format='json', indexing_type='date')
aapl, meta = ts.get_intraday(symbol='AAPL', outputsize='compact', interval='1min')

#Print stock price info
print(aapl)

print('\n')

#Print stock call info
print(meta)
