from data.classifier.source import Source
from data.classifier.asset import Asset
from data.classifier.instrument import Instrument


class Contract():
    def __init__(self,
                 source,
                 asset,
                 instrument,
                 maker_fee,
                 taker_fee,
                 commision,
                 precision_price,
                 precision_buy_qty,
                 precision_sell_qty,
                 min_stop_loss_point,
                 min_tp_point,
                 min_qty,
                 contract_size,
                 leverage
                ) -> None:
        self.source = source
        self.asset = asset
        self.instrument = instrument
        self.maker_fee = maker_fee
        self.taker_fee = taker_fee
        self.commision = commision
        self.precision_price = precision_price
        self.precision_buy_qty = precision_buy_qty
        self.precision_sell_qty = precision_sell_qty
        self.min_stop_loss_point = min_stop_loss_point
        self.min_tp_point = min_tp_point
        self.min_qty = min_qty
        self.contract_size = contract_size
        self.leverage = leverage
    
    def _get_key(self):
        return f"c_[{self.source._get_key()}]|[{self.asset._get_key()}]|[{self.instrument._get_key()}]"
    
    def _get_path(self):
        """Create a path for datasets concerning this contract
        """
    
    def _asdict(self):
        return {
            "source": self.source._asdict(),
            "asset": self.asset._asdict(),
            "instrument": self.instrument._asdict(),
            "fees": {
                "maker_fee": self.maker_fee,
                "taker_fee": self.taker_fee,    
                "commision": self.commision            
            },
            "precision":{
                "precision_price": self.precision_price,
                "precision_buy_qty": self.precision_buy_qty,
                "precision_sell_qty": self.precision_sell_qty,
            },
            "limits":{
                "min_stop_loss_point": self.min_stop_loss_point,
                "min_tp_point": self.min_tp_point,
                "min_qty": self.min_qty,
            },
            "infos":{
                "contract_size": self.contract_size,
                "leverage": self.leverage
            }
        }
        
        
        
    def get_intraday_folder_path(self, topic, year, month, day):
        return f"/home/paul/Data/{self.source._get_key()}/{self.instrument._get_key()}/{self.asset.market}_{self.asset.sub_market}/{self.base}_{self.quote}/{topic._get_key()}/intraday/" 