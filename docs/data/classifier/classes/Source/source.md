# Source

You can check the implementation [here](../../../../src/contractClassification/source.py).

## What is a source ?

A `source` is an object containing informations about the provenance of a contract such as:
- broker name
- account type

**`Arguments`:**

|argument|type|description|
|:------|:------|:------|
|broker|str|the name of the broker (ex: ftx, bybit, binance, vantageFX, interactive_broker|
|account_type|str|the type of account (ex: raw, default, ecn, standard, ...|
|tags|list[str]|list of tags to easily access a filtered sublist of existing sources|

**`Methods`:**

|method|description|
|:------|:------|
|_asdict()|generate an L1 dictionnary containing all informations about the source|
|_get_key()|generate a unique key corresponding to the source (is not tags specific)|


## Creating a source object

You can generate `Source` object using the following code:

```python
from contractClassification import source as so
source1 = so.Source(
    broker='vantageFX',
    account_type='raw',
    tags=['source_has_forex','source_has_indices']
)
```


## Generating a source object from a dictionnary

You can also reconstituate `source` object from a dictionnary (typical _asdict() output):

```python
from contractClassification import source as so
source1 = so.generate_source_from_dict(
    {
        'broker': 'name_broker',
        'account_type': 'default',
        'tags': []
    }
)
```


