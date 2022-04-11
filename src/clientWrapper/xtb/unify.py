"""
 Unification function
    transform raw output (comming directly from apy) into a unified output (according to convention)

"""
# dataset objects
from data.classifier.contract import Contract
from data.classifier.source import Source
from data.classifier.asset import Asset
from data.classifier.instrument import Perpetual
# exchange specific
from translator import Translator

TRANSLATOR = Translator()

def unify_contract(dic:dict) -> Contract:
    
    
    market=TRANSLATOR.translate_categoryName_market(dic['categoryName']), 
    sub_market=TRANSLATOR.translate_groupName_subMarket(dic['categoryName']), 
    if market == "stocks":
        base=dic['symbol'].split('.')[0]
        quote=dic['currencyProfit']
    elif market == "forex":
        base=dic['currency'] 
        quote=dic['currencyProfit']
    elif market == "indices":
        base=dic['symbol'].replace('.','_') 
        quote=dic['currencyProfit']
    elif market == "crypto":
        base=dic['currency']
        quote=dic['currencyProfit']
    elif market == "etf":
        base=dic['symbol'].split('.')[0]
        quote=dic['currencyProfit']
    elif market == "commodities":
        base=dic['symbol']
        quote=dic['currencyProfit']
        
    asset = Asset(
        base=base,
        quote=quote,
        market=market, 
        sub_market=sub_market, 
        description=dic['description'], 
        tags=[market, sub_market]
    )
    
    
    res = Contract(
        source = Source(broker="xtb", account_type='raw_demo', tags=['tradi']),
        asset=asset,
        instrument=Perpetual(margin_currency=dic['currencyProfit']),
        maker_fee=0,
        taker_fee=0,
        commision=3,
        precision_price=dic['tickSize'],
        precision_buy_qty=dic['lotStep'],
        precision_sell_qty=dic['lotStep'],
        min_stop_loss_point=dic['stopsLevel'],
        min_tp_point=dic['stopsLevel'],
        min_qty=dic['lotMin'],
        contract_size=dic['contractSize'],
        leverage=dic['leverage']
    )