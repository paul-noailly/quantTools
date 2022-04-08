# Asset

You can check the implementation [here](../../../../src/contractClassification/asset.py).

## What is a asset ?

A `asset` is an object containing informations about the underlying asset of a contract:
- broker name
- account type

**`Arguments`:**

|argument|type|description|
|:------|:------|:------|
|base|str|base ticker representing the base asset of the pair ex(EUR, APPL, BTC)|
|quote|str|quote ticker representing the quotation asset of the pair ex(EUR, APPL, BTC)|
|market|str|1st layer of classification containign information of the market (ex: forex, indices, crypto, shares, ...)|
|sub_market|str|2nd layer classification of the market (ex Forex pairs are separated into 3 categories: major, minor and exotic)|
|tags|list[str]|list of tags to easily access a filtered sublist of existing assets|

**`Methods`:**

|method|description|
|:------|:------|
|_asdict()|generate an L1 dictionnary containing all informations about the asset|
|_get_key()|generate a unique key corresponding to the asset (is not tags specific)|


## Creating a asset object

You can generate `asset` object using the following code:

```python
from contractClassification import asset as asset
asset1 = asset.Asset(
        base='EUR',
        quote='USD',
        market='forex',
        sub_market='major',
        tags=['forex','major','usd quoted','high_liquidy'],
)
```


## Generating a asset object from a dictionnary


You can also reconstituate `asset` object from a dictionnary (typical _asdict() output):

```python
from contractClassification import asset as asset
asset1 = asset.generate_asset_from_dict(
    {
        'base': 'EUR',
        'quote': 'USD',
        'market': 'forex',
        'sub_market': 'major',
        'tags': ['forex','major','usd quoted','high_liquidy']
    }
)
```