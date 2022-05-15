from django.shortcuts import render
from django.template.defaulttags import register
import os, csv
import talib
import yfinance as yf
import pandas as pd

from static.screener.patterns import candlestick_patterns

#Technical Scanner Code start 
def snapshot():
    with open('datasets/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2020-01-01", end="2020-08-01")
            data.to_csv('static/screener/datasets/daily/{}.csv'.format(symbol))

    return {
        "code": "success"
    }

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)


def techscanner(request):
    
    pattern = request.GET.get('pattern' or None)
    stocks = {}

    with open('static/screener/datasets/symbols.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern: 
        datafiles = os.listdir('static/screener/datasets/daily')
        # print(datafiles)
        for filename in datafiles:
            df = pd.read_csv('static/screener/datasets/daily/{}'.format(filename))
            # print(df)
            pattern_function = getattr(talib,pattern)
            symbol = filename.split('.')[0]

            try:
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                last = results.tail(1).values[0]
                print(last)
                # if last !=0:
                #     print("{} triggered {}".format(filename,pattern))
                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                    print (stocks[symbol])
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                    print (stocks[symbol])
                else:
                    stocks[symbol][pattern] = None
                    print (stocks[symbol])
            except :
                pass
            

    return render(request, 'techscanner.html', {'patterns': candlestick_patterns, 'stocks': stocks, 'current_pattern': pattern})
#Technical Scanner Code end
