from typing import List, Dict
import data.classifier.customTags as tags


class Topic():
    """A topic represent a kind of financial data.
    Example OHLCV-5min contain informations on:
       - timeframe (5min time interval)
       - columns: name of the columns of the dataset. Here time, open, high, low, close, volume
       - tags. List of tags
    """
    def __init__(self) -> None:
        self.timeframe = ''
        self.columns = []
        self._tags_to_add = {}
    
    
    def _asdict(self) -> Dict:
        return {
            'timeframe': self.timeframe,
            'tags': self._tags_to_add,
            'columns': self.columns,
        }
    
    def get_columns(self) -> Dict:
        return self.columns
    
    
    
class RawTick(Topic):
    def __init__(self, tick_is_based_on_bbba=True) -> None:
        super().__init__()
        self.timeframe = 'tick'
        self.tick_is_based_on_bbba = tick_is_based_on_bbba
        self.columns = ['time','bidPrice', 'askPrice']
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.contains_bbba_price,
            tags.interval_is_tick,
            tags.is_raw,
        }
        if self.tick_is_based_on_bbba:
            tags_to_add.add(tags.interval_is_tickBBBA)
        else:
            tags_to_add.add(tags.interval_is_tickTrade)
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
            
    
    
class RawCandlestick(Topic):
    def __init__(self, timeframe) -> None:
        super().__init__()
        self.timeframe = timeframe
        self.columns = ['time', 'open', 'high', 'low', 'close']
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.interval_is_time_based,
            tags.contains_ohlc,
            tags.is_raw,
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
        
        
class RawTrades(Topic):
    def __init__(self, timeframe) -> None:
        super().__init__()
        self.timeframe = 'tick'
        self.columns = ['time', 'price', 'size', 'direction', 'moved_price']
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.interval_is_tick,
            tags.contains_trade_derived_data,
            tags.is_raw,
            tags.interval_is_tickTrade
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
        
        
        
     
        
        
class Tick_BBBA_from_Trades(Topic):
    def __init__(self) -> None:
        super().__init__()
        self.timeframe = 'tick'
        self.columns = ['time', 'bidPrice', 'askPrice']
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.interval_is_tickTrade,
            tags.contains_bbba_price,
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
        
        
class OHLC(Topic):
    def __init__(self, timeframe) -> None:
        super().__init__()
        self.timeframe = timeframe
        self.columns = ['time', 'open', 'high', 'low', 'close']
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.interval_is_time_based,
            tags.contains_ohlc,
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
        
class OHLCV(Topic):
    def __init__(self, timeframe) -> None:
        super().__init__()
        self.timeframe = timeframe
        self.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.contains_volume,
            tags.interval_is_time_based,
            tags.contains_ohlc,
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
        

class OHLC_from_BBBA(Topic):
    def __init__(self, timeframe) -> None:
        super().__init__()
        self.timeframe = timeframe
        self.columns = ['time', 'open_ask', 'high_ask', 'low_ask', 'close_ask',
                        'open_bid', 'high_bid', 'low_bid', 'close_bid']
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.interval_is_time_based,
            tags.contains_ohlc,
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
        
        
class OHLCVE_from_trades(Topic):
    def __init__(self, timeframe) -> None:
        super().__init__()
        self.timeframe = timeframe
        self.columns = ['time', 'open_ask', 'high_ask', 'low_ask', 'close_ask',
                        'open_bid', 'high_bid', 'low_bid', 'close_bid', 'volume',
                        "volume_buy", "volume_sell", "prop_buy_trades", "propV_buy",
                        "pop_sell_trades", "propV_sell", "nbs_trades", "avgV_buy_price",
                        "avgV_sell_price", "avg_buy_price", "avg_sell_price",
                        "stdV_buy_price", "stdV_sell_price", "std_buy_price",
                        "std_sell_price", "avgV_price", "avg_price", "stdV_price",
                        "std_price", "avg_buy_size", "avg_sell_size",
                        "std_buy_size", "std_sell_size", "avg_size", "std_size"]
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.contains_volume,
            tags.interval_is_time_based,
            tags.contains_ohlc,
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns
        
class OHLCVE_from_trades_NVinterval(Topic):
    def __init__(self, timeframe) -> None:
        super().__init__()
        self.timeframe = timeframe
        self.columns = ['time', 'open_ask', 'high_ask', 'low_ask', 'close_ask',
                        'open_bid', 'high_bid', 'low_bid', 'close_bid', 'time_interval',
                        "volume_buy", "volume_sell", "prop_buy_trades", "propV_buy",
                        "pop_sell_trades", "prop_sell_size", "nbs_trades", "avgV_buy_price",
                        "avgV_sell_price", "avg_buy_price", "avg_sell_price",
                        "stdV_buy_price", "stdV_sell_price", "std_buy_price",
                        "std_sell_price", "avgV_price", "avg_price", "avgT_price", 
                        "stdV_price", "std_price", "avg_buy_size", "avg_sell_size",
                        "std_buy_size", "std_sell_size", "avg_size", "std_size"]
        self._tags_to_add = self.__get_tags_to_add()
                
    def __get_tags_to_add(self):
        tags_to_add = {
            tags.contains_volume,
            tags.interval_is_volume_based,
            tags.contains_ohlc,
            tags.contains_trade_derived_data,
        }
        return tags_to_add
    
    def set_columns(self, columns):
        self.columns = columns

        
