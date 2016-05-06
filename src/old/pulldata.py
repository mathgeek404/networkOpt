import pandas
import pandas.io.data as web
import datetime

#Get list of S&P stocks
df = pandas.read_csv("constituents.csv")
ticker_syms = list(df["Symbol"])

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 5, 1)

for t in ticker_syms:
  dff = web.DataReader(t, 'yahoo', start, end)
  dff.to_csv(t+"_daily.csv", sep=',', encoding='utf-8')
