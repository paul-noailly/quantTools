from utilities import baseCommand
from jsonSocket import JsonSocket
from typing import List
from checks import _check_period

from unify import unify_contract
from data.classifier.contract import Contract



class XtbRestClient(JsonSocket):
    def __init__(self, config, encrypt=True):
        super(XtbRestClient, self).__init__(config, config['clients']['xtb']['connection']['rest_port'], encrypt)
        
        self._userId = config['clients']['xtb']['credentials']['user_id']
        self._password = config['clients']['xtb']['credentials']['password']
        self._appName = config['clients']['xtb']['credentials']['app_name']
        self._address = config['clients']['xtb']['connection']['adress']
        self._port = config['clients']['xtb']['connection']['rest_port']
        self._max_conn_tries = config['clients']['xtb']['connection']['max_conn_tries']
        if(not self.connect()):
            raise Exception("Cannot connect to " + self._address + ":" + str(self._port) + " after " + str(self._max_conn_tries) + " retries")

    def _execute(self, dictionary):
        self._sendObj(dictionary)
        return self._readObj()    

    def disconnect(self):
        self.close()
        
    def _commandExecute(self,commandName, arguments=None):
        return self._execute(baseCommand(commandName, arguments))
    
    # login
    def login(self):
        return self._commandExecute("login", dict(userId=self._userId, password=self._password, appName=self._appName))
    
    def logout(self):
        return self._commandExecute("logout")
    
    # raw get: non modified get functions
    
    def rawGet_contracts(self):
        resp =  self._commandExecute("getAllSymbols")
        if resp['status']:
            return resp['returnData']
        else:
            raise Exception(f"Error on get_symbols")
    
    def rawGet_events(self):
        """return a list of events
        
        ex:
        {
            "country": "CA",
            "current": "",
            "forecast": "",
            "impact": "3",
            "period": "(FEB)",
            "previous": "58.3",
            "time": 1374846900000,
            "title": "Ivey Purchasing Managers Index"
        }
        
        Raises:
            Exception: invalid request

        Returns:
            _type_: list[dict]
        """
        resp =  self._commandExecute("getCalendar")
        if resp['status']:
            return resp['returnData']
        else:
            raise Exception(f"Error on get_symbols: {str(resp)}")
        
    def rawGet_recentCandles(self, period:int, start:int, symbol:str) -> List[dict]:
        """return a list of candlesticks from start time to most recent
        
        restrictions for periods:
        PERIOD_M1 --- <0-1) month, i.e. one month time
        PERIOD_M30 --- <1-7) month, six months time
        PERIOD_H4 --- <7-13) month, six months time
        PERIOD_D1 --- 13 month, and earlier on
        
        ex response: list of dict like:
        {
            "close": 1.0,
            "ctm": 1389362640000,
            "ctmString": "Jan 10, 2014 3:04:00 PM",
            "high": 6.0,
            "low": 0.0,
            "open": 41848.0,
            "vol": 0.0
        }

        Args:
            period (int): period in :1, 5, 15, 30, 60, 240, 1440, 10080, 43200
            start (int): Central European Time (CET) time in ms
            symbol (str): _description_

        Raises:
            Exception: _description_

        Returns:
            List[dict]: _description_
        """
        _check_period(period)
        resp =  self._commandExecute("getChartLastRequest", dict(info=dict(period=period, start=start, symbol=symbol)))
        if resp['status']:
            return resp['returnData']['rateInfos']
        else:
            raise Exception(f"Error on get_symbols: {str(resp)}")
        
        
    def rawGet_rangeCandles(self, period:int, start:int, end:int, symbol:str) -> List[dict]:
        """return a list of candlesticks
        
        restrictions for periods:
        PERIOD_M1 --- <0-1) month, i.e. one month time
        PERIOD_M30 --- <1-7) month, six months time
        PERIOD_H4 --- <7-13) month, six months time
        PERIOD_D1 --- 13 month, and earlier on
        
        ex response: list of dict like:
        {
            "close": 1.0,
            "ctm": 1389362640000,
            "ctmString": "Jan 10, 2014 3:04:00 PM",
            "high": 6.0,
            "low": 0.0,
            "open": 41848.0,
            "vol": 0.0
        }

        Args:
            period (int): period in :1, 5, 15, 30, 60, 240, 1440, 10080, 43200
            start (int): Central European Time (CET) time in ms corresponding to start of the range
            start (int): Central European Time (CET) time in ms corresponding to end of the range
            symbol (str): _description_

        Raises:
            Exception: _description_

        Returns:
            List[dict]: _description_
        """
        _check_period(period)
        resp =  self._commandExecute("getChartRangeRequest", dict(info=dict(period=period, start=start, end=end, symbol=symbol)))
        if resp['status']:
            return resp['returnData']['rateInfos']
        else:
            raise Exception(f"Error on get_symbols: {str(resp)}")
        
    def rawGet_nbsCandlesFromStart(self, period:int, start:int, bars:int, symbol:str) -> List[dict]:
        """return a list of <bars> candlesticks from start time
        
        restrictions for periods:
        PERIOD_M1 --- <0-1) month, i.e. one month time
        PERIOD_M30 --- <1-7) month, six months time
        PERIOD_H4 --- <7-13) month, six months time
        PERIOD_D1 --- 13 month, and earlier on
        
        ex response: list of dict like:
        {
            "close": 1.0,
            "ctm": 1389362640000,
            "ctmString": "Jan 10, 2014 3:04:00 PM",
            "high": 6.0,
            "low": 0.0,
            "open": 41848.0,
            "vol": 0.0
        }

        Args:
            period (int): period in :1, 5, 15, 30, 60, 240, 1440, 10080, 43200
            start (int): Central European Time (CET) time in ms corresponding to start of the range
            bars (int): number of candle to return
            symbol (str): _description_

        Raises:
            Exception: _description_

        Returns:
            List[dict]: _description_
        """
        _check_period(period)
        resp =  self._commandExecute("getChartRangeRequest", dict(info=dict(period=period, start=start, tick=bars, symbol=symbol)))
        if resp['status']:
            return resp['returnData']['rateInfos']
        else:
            raise Exception(f"Error on get_symbols: {str(resp)}")
        
        
    def rawGet_commission(self, volume:float, symbol:str) -> dict:
        """return commisions to pay for the given volume and symbol

        Args:
            volume (float): _description_
            symbol (str): _description_

        Raises:
            Exception: _description_

        Returns:
            dict: _description_
            
        Example return:
        {
            "commission": 0.51,
            "rateOfExchange": 0.1609
        }
        """
        resp =  self._commandExecute("getCommissionDef", dict(info=dict(volume=volume, symbol=symbol)))
        if resp['status']:
            return resp['returnData']
        else:
            raise Exception(f"Error on get_symbols: {str(resp)}")
        
        
        
    # unified
    
    def get_contracts(self) -> List[Contract]:
        return [unify_contract(contract_dict) for contract_dict in self.rawGet_contracts()]
        

        