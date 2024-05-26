import requests
from bs4 import BeautifulSoup
from collections import namedtuple
# import selenium

url = 'https://de.finance.yahoo.com/quote/MRK/history?period1=-252374400&period2=1716681600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0'
}

#sends request to url using headers
response = requests.get(url, headers=headers)

if (response.status_code == 200):

	soup = BeautifulSoup(response.text, 'lxml')

	data = {}
	prices = {
		"Öffnen": 0,
		"Max.": 1,
		"Min.": 2,
		"Börsenschluss*": 3,
		"Berichtigter Kurs**": 4,
		"Volumen": 5
	}

	full_line = soup.find_all('tr', class_ = 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)')
	

	#Fill dict with key:value pairs date:price
	#representing historical price data
	for i in range(len(full_line)):
		#extract date
		element_date = full_line[i].find('span').text

		# Find ALL data cells in the current row
		price_list = full_line[i].find_all('td', class_ = 'Py(10px) Pstart(10px)')
		if price_list:
			opening_price = price_list[prices["Öffnen"]].find('span').text
			max_price = price_list[prices["Max."]].find('span').text
			min_price = price_list[prices["Min."]].find('span').text
			final_price = price_list[prices["Börsenschluss*"]].find('span').text
			corrected_price = price_list[prices["Berichtigter Kurs**"]].find('span').text
			volume = price_list[prices["Volumen"]].find('span').text

		Values = namedtuple('Values',['opening_price', 'max_price', 'min_price', 'final_price', 'corrected_price', 'volume'])
		values = Values(opening_price, max_price, min_price, final_price, corrected_price, volume)

		#assign tuple of prices to the respective date 
		data[element_date] = values
	print(data)

else :
	print(f"Failed to retrieve the webpage. Status code: {response.status_code}")