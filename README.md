# scrapper

<span style="font-size: 16px;">**Stock Price Visualization Tool**</span>

This tool fetches historical stock price data for a given ticker from Yahoo Finance, saves the data in a CSV file, and visualizes the closing prices using Plotly.
Prerequisites

Make sure you have the following Python packages installed:

    requests
    plotly
    datetime
    csv
    matplotlib

# Usage

Clone the Repository:

	git clone git@github.com:Robin-Lenz/scrapper.git stock-price-visualization
	cd stock-price-visualization

Run the Script:

	python3 stock_price_visualization.py

Enter the Stock Ticker:

When prompted, enter the stock ticker symbol for the stock you want to visualize (e.g., AAPL for Apple Inc.).

View the Visualization:

The script will fetch the data, save it to a CSV file, and display an interactive line chart of the stock's closing prices.
