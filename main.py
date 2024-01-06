import backtrader as bt
import datetime as dt
from atreyu_backtrader_api import IBData

ibkr_address = '34.130.144.230'
port = 4003
client_id = 28

class TestPrinter(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.datetime(0)
        print(f'{dt}, {txt}')

    def __init__(self):
        self.open = self.datas[0].open
        self.high = self.datas[0].high
        self.low = self.datas[0].low
        self.close = self.datas[0].close
        self.volume = self.datas[0].volume
        self.openinterest = self.datas[0].openinterest

    def next(self):
        self.log(f'Open:{self.open[0]:.2f}, \
                   High:{self.high[0]:.2f}, \
                   Low:{self.low[0]:.2f}, \
                   Close:{self.close[0]:.2f}, \
                   Volume:{self.volume[0]:.2f}, \
                   OpenInterest:{self.volume[0]:.2f}')

cerebro = bt.Cerebro()

data = IBData(host=ibkr_address, port=port, clientId=client_id,
               name="GOOG",     # Data name
               dataname='BP', # Symbol name
               secType='STK',   # SecurityType is STOCK 
               exchange='SMART',# Trading exchange IB's SMART exchange 
               currency='USD',  # Currency of SecurityType
               rtbar=False,      # Request Realtime bars
               _debug=True,      # Set to True to print out debug messagess from IB TWS API,
               fromdate = dt.datetime(2016, 1, 1),
               todate = dt.datetime(2018, 1, 1),
               historical=True,
               what='TRADES',
              )

cerebro.broker.setcash(10000.0)
cerebro.broker.setcommission(commission=0.001)
cerebro.addstrategy(TestPrinter)
cerebro.adddata(data)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
