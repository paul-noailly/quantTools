#  Data Manager

## Table Of Content

  - [1 - Why this package ?](#1---why-this-package-)
  - [2 - Contents](#2---contents)
  - [3 - How to use ?](#3---how-to-use-)
    - [3.1 - How to install ?](#31---how-to-install-)
    - [3.2 - Configuration file](#32---configuration-file)
    - [3.3 - Quick start](#33---quick-start)
  - [4 - Contribute](#4---contribute)
  - [5 - Todo List](#5---todo-list)
  - [6 - Usefull ressources](#6---usefull-ressources)
  - [7 - Similar projects](#7---similar-projects)


## 1 - Why this package ?

**Problem:**

Building a quantitative strategy is a complex process that involve working on financial datasets, implementing a wrapper to interact with the broker, and then implementing a backtester for the strategy, as well as optimization & visualization scripts.

When backtesting multiple strategies on multiple assets & brokers, it can quickly become extremely redondant and time-consuming if you have to remake broker bridges, importing the data & rewritting backtesting scripts from scratch.

If you want to be more efficient you need robust & polyvalent libraries/workflows that you can use every time no mater the broker, type of data, or type of strategy.

This is exactly what this package aims to be: a collection of tools that can be used on multiple quantitative works.

**Solutions:**

- Simplify the data collection process
  - Classification methodology to cover all kinds of datasets
  - scraping scripts
  - transformation scripts for better automation
- Simplify interaction with brokers with a unified client wrapper (RESt & stream)
- Provide quantitative tools: optimization, multi-threading, visualization of backtest outputs
- Provide specific backtesters for some key strategies (ex: statistical arbitrage, signal based swing strategies, market making, ...)


## 2 - Contents Organisation

List and purposes of all files and folders within this project.

|Folder/File|Description|
|:------|:------|
|[`docs/`](docs)|Documentation of the project|
|[`tests/`](tests)|Tests of the project|
|[`src/`](src)|Source folder|


This package contains 3 sub-packages: 

|Sub-package|Documentation|Description|
|:------|:------|:------|
|[`src/data`](src/data)|[`docs/data`](docs/data)|data related sub-package designed to download, scrape, transform, visualize & access data easily|
|[`src/clientWrapper`](src/clientWrapper)|[`docs/clientWrapper`](docs/clientWrapper)|A unified client (for REST request & Stream clients) as well as specific clients for many brokers (crypto+traditional)|
|[`src/strategy`](src/strategy)|[`docs/strategy`](docs/strategy)|Implementation of quantitative tools (optimization, multi-threading, visualization,..) as well as generalized strategy implementation for popular strategy types (statisticalarbitrage, market making, indicator based swing strategy,..)|

### 2.1 - Data sub-package


|Module|Documentation|Description|
|:------|:------|:------|
|[`src/data/classifier`](src/data/classifier)|[`docs/data/classifier`](docs/data/classifier)|Methodology & Tools to rigourously classify any financial dataset in term of source, topic, instrument & underlying assets|
|[`src/data/scraper`](src/data/scraper)|[`docs/data/scraper`](docs/data/scraper)|Module for scraping live data & historical (publicly available) data|
|[`src/data/transformer`](src/data/transformer)|[`docs/data/transformer`](docs/data/transformer)|Module for transforming existing data into new enrichied modified data (volum based candlesticks, enriched candlestick from historical trades, ...)|
|[`src/data/vizualizer`](src/data/vizualizer)|[`docs/data/vizualizer`](docs/data/vizualizer)|Tools to vizualize financial datasets|


### 2.2 - clientWrapper sub-package


|Module|Documentation|Description|
|:------|:------|:------|
|[`src/clientWrapper/unifiedClient`](src/clientWrapper/unifiedClient)|[`docs/clientWrapper/unifiedClient`](docs/clientWrapper/unifiedClient)|A unified client, with unified outputs no matter the broker source|
|[`src/clientWrapper/xtb`](src/clientWrapper/xtb)|[`docs/clientWrapper/xtb`](docs/clientWrapper/xtb)|Implementation of rest & stream client specific to xtb|
|[`src/clientWrapper/binance`](src/clientWrapper/binance)|[`docs/clientWrapper/binance`](docs/clientWrapper/binance)|Implementation of rest & stream client specific to binance|
|[`src/clientWrapper/ftx`](src/clientWrapper/ftx)|[`docs/clientWrapper/ftx`](docs/clientWrapper/ftx)|Implementation of rest & stream client specific to ftx|
|[`src/clientWrapper/bybit`](src/clientWrapper/bybit)|[`docs/clientWrapper/bybit`](docs/clientWrapper/bybit)|Implementation of rest & stream client specific to bybit|

more exchanges coming

### 2.3 - strategy sub-package


|Module|Documentation|Description|
|:------|:------|:------|
|[`src/strategy/quantTools`](src/strategy/quantTools)|[`docs/strategy/quantTools`](docs/strategy/quantTools)|Implementation of tools for optimisation (rolling, bayesian, ..), multi-threading, ...|
|[`src/strategy/marketMakingStandard`](src/strategy/marketMakingStandard)|[`docs/strategy/marketMakingStandard`](docs/strategy/marketMakingStandard)|Module for a standard market making strategy|
|[`src/strategy/statisticalArbitrageStandard`](src/strategy/statisticalArbitrageStandard)|[`docs/strategy/statisticalArbitrageStandard`](docs/strategy/statisticalArbitrageStandard)|Module for a standard statistical arbitrage strategy (zscore + break out or pull back for entries & exit)|




## 3 - How to use ?

How to use this package ?

### 3.1 - How to install ?

How to install this package ?

```ssh
pip install git+https://github.com/paul-noailly/dataManager
```

<!-- or


```ssh
git clone https://github.com/paul-noailly/dataManager
sudo python setup.py install
``` -->

### 3.2 - Configuration file

You need a configuration file to run most things from this distribution.
This file is a json file named `config_<project_name>.json`. 
The path can be specified in most classes. By default it is in the execution folder.
The content of the json config file should be as follows:

|Key|Description|
|:------|:------|
|param1|Descritpion param1|

### 3.3 - Quick start

This is some indication for the most basic features.
For more details, see [`docs/`](docs).

```python
from distribution import package1
from distribution.package1 import class1
```

## 4 - Contribute

How to contribute to this project ?

```ssh
git add . && git commit -m "name commit" && git push origin master
```

## 5 - Todo List

Tasks done and planned related to this project.

- [ ] clients wrapper
  - [ ] crypto
    - [ ] centralized
      - [ ] ftx
      - [ ] bybit
      - [ ] fxcm
      - [ ] binance
    - [ ] decentralized
      - [ ] uni
  - [ ] traditional
    - [ ] xtb
      - [x] architecture
      - [x] raw requests rest
      - [ ] unified requests rest
    - [ ] mt5 client (windows only - cancel ?)
    - [ ] IB client
    - [ ] cmarket client
  - [ ] unified client 
- [ ] data
  - [ ] classifier
    - [x] doc classification process
    - [x] implement assets + docs
    - [x] implement source + docs
    - [x] implement topics + docs
    - [x] implement instrument + docs
    - [ ] implement contract + docs
    - [ ] implement dataset + docs
    - [ ] advanced testing
    - [ ] fix packaging
  - [ ] dataScraper
    - [ ] storage solution
    - [ ] liveScraper
    - [ ] historicalScraper
  - [ ] dataTransformer
    - [ ] resampling
    - [ ] bbba from trades
    - [ ] ohlcve from trades
    - [ ] auto routines
  - [ ] dataViz
  - [ ] manager
    - [ ] visualize stored data easily
    - [ ] 
- [ ] strategy
  - [ ] tools
    - [ ] visualize strategy metrics
    - [ ] rolling parameter bayesian optimisation
    - [ ] multi threading
  - [ ] statistical arbitrage classic backtester

## 6 - Usefull ressources

List of usefull ressources related to this project.

## 7 - Similar projects

List of similar projects ?


