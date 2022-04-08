from typing import List, Dict


def generate_asset_from_dict(dic:Dict):
    assert 'base' in dic, "dic parameter must contain a base:str item"
    assert 'quote' in dic, "dic parameter must contain a quote:str item"
    assert 'market' in dic, "dic parameter must contain a market:str item"
    assert 'sub_market' in dic, "dic parameter must contain a sub_market:str item"
    assert 'tags' in dic, "dic parameter must contain a tags:List[str] item"
    return Asset(
        base=dic['base'],
        quote=dic['quote'],
        market=dic['market'],
        sub_market=dic['sub_market'],
        tags=dic['tags'],
    )

class Asset():
    """Asset
    class that defines an Asset entity like EURUSD
    EURUSD has:
    - base : a base currency: EUR
    - quote : a quote currency: USD
    - market : a market: Forex
    - sub_market : a sub market: Major    
    - tags : a list of tags.
    """
    def __init__(self, base:str, quote:str, market:str=None, sub_market:str=None, tags:list=[]) -> None:
        self.quote = quote
        self.base = base
        self.market = market
        self.sub_market = sub_market
        self.tags = tags
        
    def _asdict(self):
        return {
            'base': self.base,
            'quote': self.quote,
            'market': self.market,
            'sub_market': self.sub_market,
            'tags': self.tags
        }
        
    def _get_key(self):
        return f"a_{self.base}|{self.quote}|{self.market}|{self.sub_market}"
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"Asset[ {self.base}/{self.quote} - {self.market}/{self.sub_market} ]".replace('None','')