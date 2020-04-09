import yfinance as yf 
import matplotlib.pyplot as plt
import seaborn as sns


class Stock: 
    def __init__(self,stockname, period):
        stock = yf.Ticker(stockname)
        self.history = stock.history(period=period)
        self.period = period 

    def plot(self):
        plt.plot(self.history['Close'])
        plt.show()

    def downloadCSV(self):
        data_df = yf.download(stockname, period=self.period)
        data_df.to_csv(stockname.lower() + '.csv')
    

if __name__ == "__main__":
    # execute only if run as a script
    #handle input from command lines
    stockname = input("What stock would you like to analyze? \n")
    period = input ("Enter a time period, ex. '', 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max \n")
    stock = Stock(stockname,period)
    print(stock.history)
    shouldPlot = input("Would you like to plot the history? : ")
    if shouldPlot.lower() == 'y': 
        stock.plot()

    convertToCSV = input("Would you like to download the history as a CSV file? : ")
    if convertToCSV.lower() == 'y':
        stock.downloadCSV()
        print("The CSV file is located within the projects directory.")