import requests
import matplotlib.pyplot as plt
import csv

import plotly.graph_objs as go
import plotly.io as pio
from datetime import datetime

ticker = input("Enter a stockticker: ")

###send request and save file
url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=-252374400&period2=1716768000&interval=1d&events=history&includeAdjustedClose=true"


headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0'
}

#sends request to url using headers
response = requests.get(url, headers=headers)

if (response.status_code == 200):

	# Save the content to a file
	with open(f"{ticker}.csv", 'wb') as file:
		file.write(response.content)
	print('File downloaded successfully')

else :
	print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


###read from file and store data in arrays
x = []
y = []

#extract data from csv
with open(f"{ticker}.csv", mode='r', newline='') as csv_file:
	csv_reader = csv.reader(csv_file)

	# Skip the header row
	next(csv_reader)

	#fill y with dates
	for row in csv_reader :
		date_str = row[0]
		date_obj = datetime.strptime(date_str, '%Y-%m-%d')
		x.append(date_obj)
		y.append(float(row[2]))


###visualization

#create figure obj
fig = go.Figure(data=go.Scattergl(x=x, y=y, mode='lines'))

# Add titles and labels
fig.update_layout(yaxis_tickmode='auto',
				title='Price graph',
				xaxis_title='Date',
				yaxis_title='Price',
				width=2000,
				height=1000)

pio.show(fig)
