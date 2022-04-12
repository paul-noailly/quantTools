from typing import List, Dict



class Instrument():
    def __init__(self, tags:List[str]=[]) -> None:
        self.tags = tags
        
    def _get_key(self):
        return f"s_{self.broker}|{self.account_type}"
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"instrument[ {self.broker} - {self.account_type} ]"
    
    
class Spot():
    def __init__(self) -> None:
        self.type = 'spot'
    
    def _asdict(self):
        return {
            "type": self.type
        }
        
    def _get_key(self):
        return f"i_{'|'.join([str(v) for k,v in self._asdict().items()])}"
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"Instrument[ {self._get_key()[2:]} ]".replace('|',' - ')
    

class Option():
    def __init__(self, type:str, 
                 strike:float, 
                 margin_currency:str, 
                 expiration_time_utc:float, 
                 launch_time_utc:float) -> None:
        """Generate Option Instrument

        Args:
            type (str): within [call, put, straddle, binary]
            strike (float): strike price
            margin_currency (float): margin currency used to buy & sell contract
            expiration_time_utc (float): utc time in sec at whcih contract will terminate
            launch_time_utc (float): utc time in sec at whcih contract was initiated
        """
        self.type = type
        self.strike = strike
        self.margin_currency = margin_currency
        self.expiration_time_utc = expiration_time_utc
        self.launch_time_utc = launch_time_utc
    
    def _asdict(self):
        return {
            "type": self.type,
            "strike": self.strike,
            "margin_currency": self.margin_currency,
            "expiration_time_utc": self.expiration_time_utc,
            "launch_time_utc": self.launch_time_utc,
            
        }
        
    def _get_key(self):
        return f"i_{'|'.join([str(v) for k,v in self._asdict().items()])}"
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"Instrument[ {self._get_key()[2:]} ]".replace('|',' - ')



class Perpetual():
    def __init__(self, margin_currency:str) -> None:
        """Generate Perpetual swap Instrument

        Args:
            margin_currency (float): margin currency used to buy & sell contract
        """
        self.type = "perpetual"
        self.margin_currency = margin_currency
    
    def _asdict(self):
        return {
            "type": self.type,
            "margin_currency": self.margin_currency,
        }
        
    def _get_key(self):
        return f"i_{'|'.join([str(v) for k,v in self._asdict().items()])}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"Instrument[ {self._get_key()[2:]} ]".replace('|',' - ')


class Future():
    def __init__(self, 
                 margin_currency:str, 
                 expiration_time_utc:float, 
                 launch_time_utc:float) -> None:
        """Generate Future Instrument

        Args:
            margin_currency (float): margin currency used to buy & sell contract
            expiration_time_utc (float): utc time in sec at whcih contract will terminate
            launch_time_utc (float): utc time in sec at whcih contract was initiated
        """
        self.type = "future"
        self.margin_currency = margin_currency
        self.expiration_time_utc = expiration_time_utc
        self.launch_time_utc = launch_time_utc
    
    def _asdict(self):
        return {
            "type": self.type,
            "margin_currency": self.margin_currency,
            "expiration_time_utc": self.expiration_time_utc,
            "launch_time_utc": self.launch_time_utc,
            
        }
        
    def _get_key(self):
        return f"i_{'|'.join([str(v) for k,v in self._asdict().items()])}"
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"Instrument[ {self._get_key()[2:]} ]".replace('|',' - ')


class Token():
    def __init__(self,
                 multiplier:float, 
                 margin_currency:str, ) -> None:
        """Generate Token Instrument

        Args:
            multiplier (float): multiplier of the token
            margin_currency (float): margin currency used to buy & sell contract
        """
        self.type = "token"
        self.margin_currency = margin_currency
        self.multiplier = multiplier
    
    def _asdict(self):
        return {
            "type": self.type,
            "multiplier": self.multiplier,
            "margin_currency": self.margin_currency,
            
        }
        
    def _get_key(self):
        return f"i_{'|'.join([str(v) for k,v in self._asdict().items()])}"
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"Instrument[ {self._get_key()[2:]} ]".replace('|',' - ')


