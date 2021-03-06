Trading Bot by Carlo Guzman & Ryan Borunda

Goal: Create a profitable automated trading bot that tracks (desired?) stocks

Steps:
	1) Find an API
		* Using AlphaVantage
		* Check documentation here: https://www.alphavantage.co/documentation/
		* More here: https://github.com/RomelTorres/alpha_vantage
	2) Find relevant stocks
		* Possible method of approach:
			* Find five fastest growing stocks every day here:
			https://finance.yahoo.com/gainers
			* Web-scrape for those five stocks w/ selenium read more here: 				https://dev.to/lewiskori/beginner-s-guide-to-web-scraping-with-python-s-selenium-3fl9
			* Call API on each of the five stocks every minute
			* Track live price of stock
			* Employ trading strategy, possible strategies below
		* https://www.investopedia.com/articles/trading/06/daytradingretail.asp
		* https://www.investopedia.com/articles/active-trading/090415/only-take-trade-if-it-passes-5step-test.asp
Resources:

	1) Rob Carver, Phyton Trading Blog
		*https://qoppac.blogspot.com/p/about-me.html
	2) Doji Method:
	https://www.investopedia.com/terms/d/doji.asp
	3) https://www.quantopian.com/home 
		*"Quantopian provides free education, data, and tool so anyone can pursue quantitative finance"
	4) Warren Buffet's "Stock"Cheat Sheet Checklist:
		*https://www.reddit.com/r/investing/comments/bpriju/the_ultimate_investing_checklist/?utm_source=share&utm_medium=ios_app
Strategies:

	1) 15+ Asset Management Strategies
		*https://github.com/firmai/machine-learning-asset-management
	2) Put/Call (Safe) Strategy
		* Finding historically safe stocks (e.g. Walmart, Coca-Cola), purchase stock on stock dip and sell
after any drop in 5%
		* Hold dividend-rich stocks (e.g. AT&T) and reinvest dividents into itself or safe stocks
		
		~PROS:
		~CONS:

		
		
