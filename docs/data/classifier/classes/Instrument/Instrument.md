# Instrument

You can check the implementation [here](../../../../src/contractClassification/instrument.py).

## What is a instrument ?

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

**`Arguments`:**

Arguments depend on the nature of the `Instrument`. (cf [here](../Instrument/))

**`Methods`:**

|method|description|
|:------|:------|
|_asdict()|generate an L1 dictionnary containing all informations about the instrument|
|_get_key()|generate a unique key corresponding to the instrument (is not tags specific)|
```