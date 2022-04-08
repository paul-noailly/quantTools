# Classification process

## Data Identification process

Data coming from any broker is caracterized by many features:
- `Source` : broker, type of account (raw, standard, ..)
- `underlying asset` (ex: EURUSD, BTCUSD, SPY, collection of assests, ...)
- `topic`: bid-ask tick datas, 5min ohlcv condelsticks, orderbook, ...
- `Instrument`: The type of contract and its caracteristics. ex: spot contract, perpetual swaps with margin in USDT, call option with maturity 07/2024 and strike 7$, ...

Each of these features are implemented as independant object.
Then a contract is also an object that takes each of these independent objects as arguments.








## Topics

### What is a topic ?

We call `topic` the type of financial data given its source, underlying asset and instrument.
It contain information about data's columns, and interval of data (ticks, 1 minute, ...).

A `topic` can be "raw", meanning the data comes directly from the source without any transformation. Or it can be transformed into a new topic.

Topics that are transformed are unified, meanning their data columns are the same, no matter the `source`, the `underlying` or the `instrument`.

For example a topic can be `raw tick best bid best ask`, `raw candlestick 5min`, `order book 10 levels 10s`

### List of implemented topics

You can see the full list of implemented topics structure [here](topics_list.md).

### Example of use

```python
from contractClassification import topic as tp
# raw ticks: best bid - best ask
topic = tp.RawTick()
# raw candlestick
topic = tp.RawCandlestick(timeframe='1m')
# unified tick best bid best ask
topic = tp.Tick_BBBA()
# unified ohlcv
topic = tp.OHLCV(timeframe='1h')
# unified ohlcv with best bid best ask
topic = tp.OHLCV_from_BBBA(timeframe='5s')
# unified enriched ohlcv from trades
topic = tp.OHLCVE_from_Trades(timeframe='5s')
# unified enriched ohlcv from trades with interval based on notional value
topic = tp.OHLCV_from_Trades_NVinterval(interval='1000')
# unified order books base on levels of prices
topic = tp.OB_priceStep(timeframe='10s', levels=10, increment=0.5)
# unified order books based on % of size
topic = tp.OB_percentSizeStep(timeframe='10s', levels=20, increment=0.01)
```







## Asset

### What is an Asset ?

An `Asset` is defined by the quote and the base of any financial pair. \
For example the pair EURUSD represent an asset of base EUR and quote USD, which value at time t is how much USD is worth 1 EUR.

This concept is mainly usefull for pairs trading or any kind of multi assets trading where you want to compare 2 quotation of the same pair, base or quote.

It also contain information such as the category & sub category of the market.
For example:
|Symbol|Market|Submarket|
|:------|:------|:------|
|EURUSD|forex|major|
|EURGBP|forex|minor|
|USDSEK|forex|exotic|
|BTCUSD|crypto|major|
|FTTUSD|crypto|exchange|

### Implementation

An `Asset` object have been implemented. (see documentation [here](./classes/Asset/Asset.md))



## Source 

### What is a source ?

A source is all the information concerning the provenance of the financial datasets. 
It contains information about:
  - the broker
  - the type of account (raw, ecn, standard, default ...)

Some data differs even if they come from the same broker. \
That is usually the case for Forex broker that have different account: Raw account for zero spread but commission, and Standard account that have zero commission but a noticable spread.

### Implementation

A `Source` class have been implemented [here](../../src/contractClassification/source.py). You can also check the doc on [here](./classes/Source/)



## Instrument 

### What is an instrument ?

An `instrument` is an object containing informations about the technical specificities of a contract. \
There exist many types and subtypes of `instrument`, each with different parameters
- `spot`:  most basic instrument, buy or sell physical base asset, using quote asset
- `options`: depend on strike, maturity, launch_date
  - `call`: 
  - `put`: 
  - `straddle`: (currently only straddle with 1 strike is implemented)
  - `binary`: 
- `future`: 
  - `expirable`: standard future, with expiration date
  - `perpetual swap`: no expiration date, buy contract with `margin currency`
- `token`: tokenized version of an asset, using a multiplier (x-1 are hedge token, x3 are bull token, x-3 are bear token, x0.5 are half token, ...). token are digital contract that mimic the price action of an underlying asset, often with a multiplier.

### Implementation

Each used instrument are implemented into an object. You can check the doc on Instruments [here](classes/Instrument.md)






## Contract 

### What is a contract ?

A contract is a unique object that is based on the, underlying `asset`, `source`, `instrument` but not on the topic, dates ect... \
Identifying the contract the just step just before ending the classification with the `topic` object