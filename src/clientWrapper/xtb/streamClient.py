
import json
import socket
import logging
import time
import ssl
from threading import Thread

from jsonSocket import JsonSocket

from utilities import procTickMsgPrinter, procTradeMsgPrinter, procBalanceMsgPrinter, procTradeStatusMsgPrinter, procProfitMsgPrinter, procNewsMsgPrinter




    
class XtbStreamClient(JsonSocket):
    def __init__(self, config, encrypt=True, ssId=None, 
                 tickMsgPrinter=procTickMsgPrinter, tradeMsgPrinter=procTradeMsgPrinter, balanceMsgPrinter=procBalanceMsgPrinter, 
                 tradeStatusMsgPrinter=procTradeStatusMsgPrinter, profitMsgPrinter=procProfitMsgPrinter, newsMsgPrinter=procNewsMsgPrinter):
        super(XtbStreamClient, self).__init__(config, config['clients']['xtb']['connection']['stream_port'], encrypt)
        self._ssId = ssId

        self._tickMsgPrinter = tickMsgPrinter
        self._tradeMsgPrinter = tradeMsgPrinter
        self._balanceMsgPrinter = balanceMsgPrinter
        self._tradeStatusMsgPrinter = tradeStatusMsgPrinter
        self._profitMsgPrinter = profitMsgPrinter
        self._newsMsgPrinter = newsMsgPrinter
        
        # connection
        self._address = config['clients']['xtb']['connection']['adress']
        self._port = config['clients']['xtb']['connection']['stream_port']
        self._max_conn_tries = config['clients']['xtb']['connection']['max_conn_tries']
        
        if(not self.connect()):
            raise Exception("Cannot connect to streaming on " + self._address + ":" + str(self._port) + " after " + str(self._max_conn_tries) + " retries")

        self._running = True
        self._t = Thread(target=self._readStream, args=())
        self._t.setDaemon(True)
        self._t.start()

    def _readStream(self):
        while (self._running):
                msg = self._readObj()
                #logger.info("Stream received: " + str(msg))
                if (msg["command"]=='tickPrices'):
                    self._tickMsgPrinter(msg)
                elif (msg["command"]=='trade'):
                    self._tradeMsgPrinter(msg)
                elif (msg["command"]=="balance"):
                    self._balanceMsgPrinter(msg)
                elif (msg["command"]=="tradeStatus"):
                    self._tradeStatusMsgPrinter(msg)
                elif (msg["command"]=="profit"):
                    self._profitMsgPrinter(msg)
                elif (msg["command"]=="news"):
                    self._newsMsgPrinter(msg)
    
    def disconnect(self):
        self._running = False
        self._t.join()
        self.close()

    def execute(self, dictionary):
        self._sendObj(dictionary)

    def subscribePrice(self, symbol):
        """subscribe to prices of 1 symbol

        Args:
            symbols (_type_): list of tickers. ex: 'EURUSD'
        """
        self.execute(dict(command='getTickPrices', symbol=symbol, streamSessionId=self._ssId))
        
    def subscribePrices(self, symbols):
        """subscribe to prices of multiples symbols

        Args:
            symbols (_type_): list of tickers. ex: ['EURUSD', 'EURGBP', 'EURJPY']
        """
        for symbolX in symbols:
            self.subscribePrice(symbolX)
    
    def subscribeTrades(self):
        self.execute(dict(command='getTrades', streamSessionId=self._ssId))
        
    def subscribeBalance(self):
        self.execute(dict(command='getBalance', streamSessionId=self._ssId))

    def subscribeTradeStatus(self):
        self.execute(dict(command='getTradeStatus', streamSessionId=self._ssId))

    def subscribeProfits(self):
        self.execute(dict(command='getProfits', streamSessionId=self._ssId))

    def subscribeNews(self):
        self.execute(dict(command='getNews', streamSessionId=self._ssId))


    def unsubscribePrice(self, symbol):
        self.execute(dict(command='stopTickPrices', symbol=symbol, streamSessionId=self._ssId))
        
    def unsubscribePrices(self, symbols):
        for symbolX in symbols:
            self.unsubscribePrice(symbolX)
    
    def unsubscribeTrades(self):
        self.execute(dict(command='stopTrades', streamSessionId=self._ssId))
        
    def unsubscribeBalance(self):
        self.execute(dict(command='stopBalance', streamSessionId=self._ssId))

    def unsubscribeTradeStatus(self):
        self.execute(dict(command='stopTradeStatus', streamSessionId=self._ssId))

    def unsubscribeProfits(self):
        self.execute(dict(command='stopProfits', streamSessionId=self._ssId))

    def unsubscribeNews(self):
        self.execute(dict(command='stopNews', streamSessionId=self._ssId))