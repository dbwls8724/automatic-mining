import requests
from bs4 import BeautifulSoup as bs
from time import sleep

URL='https://www.antpool.com/user/settings.htm'
data_to_BTC = {'m':'account', 'id':'*******','btcAddr':'***************************',\ #Copy and paste your data
'miningCoin':'BTC','paymentMethod': '0',\
'setCoin': '',\
'btcMinimumPayment': '0.05',\
'bccMinimumPayment': '0.001', 'btcAddrLock':'1', 'nickname':'', 'bccAddr':''} 


data_to_BCC = {'m':'account', 'id':'*******','btcAddr':'***************************',\ #Copy and paste your data
'miningCoin':'BCC','paymentMethod': '0',\
'setCoin': '',\
'btcMinimumPayment': '0.05',\
'bccMinimumPayment': '0.001', 'btcAddrLock':'1', 'nickname':'', 'bccAddr':''} 


header={
'Host': 'www.antpool.com',
'Connection': 'keep-alive',
'Content-Length': '185',
'Accept': '*/*',
'Origin': 'https://www.antpool.com',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Referer': 'https://www.antpool.com/user/settings.htm',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': '********', #Copy and paste the accept language
'Cookie': '********', #Copy and paste your cookie
'DNT': '1'}

while(1):
	profit_page = requests.get('https://cash.coin.dance/blocks')
	html = profit_page.text
	soup = bs(html, 'html.parser')
	amount = soup.find_all('h4', {'title': 'Profitability takes into account the following metrics:<ul><li>Price</li><li>Difficulty</li><li>Block reward (block subsidy + transaction fees)</li></ul>'}) 
	amount=str(amount[0])
	profitable=amount.find("Bitcoin (BTC) chain")
	
	if profitable==-1:
		res = requests.post(URL, headers=header, data=data_to_BCC)
	else:	
		res = requests.post(URL, headers=header, data=data_to_BTC)

	sleep(5)
