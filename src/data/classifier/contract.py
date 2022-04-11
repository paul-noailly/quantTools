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
                 precision_price,
                 precision_buy_qty,
                 precision_sell_qty,
                 min_stop_loss_point,
                 min_tp_point,
                 contract_size
                ) -> None:
        self.source = source
        self.asset = asset
        self.instrument = instrument
        self.maker_fee = maker_fee
        self.taker_fee = taker_fee
        self.precision_price = precision_price
        self.precision_buy_qty = precision_buy_qty
        self.precision_sell_qty = precision_sell_qty
        self.min_stop_loss_point = min_stop_loss_point
        self.min_tp_point = min_tp_point
        self.contract_size = contract_size
    
    def _get_key(self):
        return f"c_[{self.source._get_key()}]|[{self.asset._get_key()}]|[{self.instrument._get_key()}]"
    
    def _get_path(self):
        """Create a path for datasets concerning this contract
        """
    
    def _asdict(self):
        return {
            "source": self.source,
            "asset": self.asset,
            "instrument": self.instrument,
            "fees": {
                "maker_fee": self.maker_fee,
                "taker_fee": self.taker_fee,                
            },
            "precision":{
                "precision_price": self.precision_price,
                "precision_buy_qty": self.precision_buy_qty,
                "precision_sell_qty": self.precision_sell_qty,
            },
            "limits":{
                "min_stop_loss_point": self.min_stop_loss_point,
                "min_tp_point": self.min_tp_point,
            },
            "infos":{
                "contract_size": self.contract_size
            }
        }