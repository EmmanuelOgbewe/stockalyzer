import yfinance as yf 
import matplotlib.pyplot as plt


def readFile(directory,stockname):
    with open((stockname.lower() + '.csv'), 'r') as f:
        return f.read()

def writeToFile(path, stockname):
    data = readFile(path,stockname)
    if not '/' in path[-1]:
        path_to_write = path + '/' + stockname.lower() + '.csv'
    else:
        path_to_write = path + stockname.lower() + '.csv'

    with open(path_to_write, 'w') as f:
        f.write(data)
    print("The CSV file was written to " + path_to_write + '.')


class Stock: 
    def __init__(self,stockname, period):
        stock = yf.Ticker(stockname)
        self.history = stock.history(period=period)
        self.period = period 

    def plot(self):
        plt.plot(self.history['Close'])
        plt.xlabel('Date')
        plt.ylabel('Close Cost')
        plt.show()

    def downloadCSV(self):
        data_df = yf.download(stockname, period=self.period)
        data_df.to_csv(stockname.lower() + '.csv')


if __name__ == "__main__":
    # execute only if run as a script
    #handle input from command lines
    stockname = input("What stock would you like to analyze? ex. AAPL, MSFT, TWTR \n")
    period = input ("Enter a time period, ex. '', 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max \n")
    stock = Stock(stockname,period)
    print(stock.history)
    shouldPlot = input("Would you like to plot the history? y | n : ")
    if shouldPlot.lower() == 'y': 
        stock.plot()

    convertToCSV = input("Would you like to download the history as a CSV file?  y | n : ")
    if convertToCSV.lower() == 'y':
        path = input("Please type in a valid path to write the file to: \n")
        stock.downloadCSV()
        if len(path) != 0: 
            writeToFile(path,stockname)
        else:
            print("The CSV file is located within the projects directory.")
        