import enum
import os


class MARKET(enum.Enum):
    FX = 'forex'
    STOCKS = 'stocks'
    COMMODITIES = 'commodities'
    INDICES = 'indices'
    ETF = 'etf'
    CRYPTO = 'crypto'