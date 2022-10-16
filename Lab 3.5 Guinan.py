#!/usr/bin/env python
# coding: utf-8

# In[170]:


get_ipython().system('pip install yfinance')


# In[276]:


import json
import requests
import pandas
import yfinance as yf
from datetime import date


# In[285]:


stock =input()
today = date.today().strftime('%Y-%m-%d')


# In[286]:


url = 'https://query1.finance.yahoo.com/v7/finance/quote'

url3 = 'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{0}?modules=financialData'.format(stock)


# In[287]:


querystring = {"symbols": stock}


# In[288]:


header_var ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.request("GET",url, headers=header_var,params=querystring)

response3 = requests.request("GET",url3, headers=header_var,params=querystring)


# In[289]:


stock_json = response.json()
stock_json1 = response3.json()


# In[290]:


if len(stock_json['quoteResponse']['result']) == 0:
    print("Sorry there has been an error.  Check if this stock exists")
else: 
    sjson = stock_json['quoteResponse']['result'][0]['longName']
    sjson3 = stock_json1['quoteSummary']['result'][0]['financialData']['currentPrice']['raw']
    sjson4 = stock_json1['quoteSummary']['result'][0]['financialData']['targetMeanPrice']['raw']
    sjson5 = stock_json1['quoteSummary']['result'][0]['financialData']['totalCash']['fmt']
    sjson6 = stock_json1['quoteSummary']['result'][0]['financialData']['profitMargins']['fmt']
    print(stock, ',' ,sjson, ',' ,sjson3,',', sjson4, ',', sjson5, ',', sjson6)
    stock_data = {}
    stock_data['stock'] = {'name ticker' : stock, 'full name' : sjson, 'current price' : sjson3, 'target mean price' : sjson4, 'cash' : sjson5, 'profit margins' : sjson6, 'date pulled' : today}
    with open('mydata.json', 'w') as f:
        json.dump(stock_data, f)
    f = open('mydata.json')
    stock_data = json.load(f)
    print(stock_data['stock'])









# In[ ]:




