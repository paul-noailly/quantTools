from clientWrapper.unified.enums import MARKET

class Translator(object):
    groupName_subMarket = {
        # commodities
        'Agriculture': 'Agriculture',
        'Energy': 'Energy',
        'Industrial Metals': 'Industrial Metals',
        'Livestock': 'Livestock',
        'Other': 'Other',
        'Precious Metals': 'Precious Metals',
        # indicies
        'Americas': 'US', 
        'Asia-Pacific': 'ASIA', 
        'Europe': 'EU',
        # etfs
        'ETF': 'ETF', 
        'ETFs': 'ETFs',
        # stock
        'Belgium': 'Belgium',
        'Czech Rep.': 'CzechRep',
        'Denmark': 'Denmark',
        'Finland': 'Finland',
        'France': 'France',
        'Germany': 'Germany',
        'Italy': 'Italy',
        'Netherlands': 'Netherlands',
        'Norway': 'Norway',
        'Poland': 'Poland',
        'Portugal': 'Portugal',
        'Spain': 'Spain',
        'Sweden': 'Sweden',
        'Switzerland': 'Switzerland',
        'UK': 'UK',
        'US': 'US',
        # forex
        'Emergings': 'Emergings', 
        'Major': 'Major', 
        'Minor': 'Minor'
        
    }
    categoryName_market = {
        'ETF':MARKET.ETF.value, 
        'CMD':MARKET.COMMODITIES.value, 
        'IND':MARKET.INDICES.value, 
        'CRT':MARKET.CRYPTO.value, 
        'STC':MARKET.STOCKS.value, 
        'FX': MARKET.FX.value}
    
    symbolIndice = {
        'US500.cash': 'US500.cash',
        'BRAComp': 'BRAComp',
        'US100': 'US100',
        'VIX': 'VIX',
        'US500': 'US500',
        'US30': 'US30',
        'US100.cash': 'US100.cash',
        'US2000': 'US2000',
        'US30.cash': 'US30.cash',
        'USFANG': 'USFANG',
        'VOLX': 'VOLX',
        'MEXComp': 'MEXComp',
    }
    
    def translate_categoryName_market(self, val):
        if val in Translator.categoryName_market:
            return Translator.categoryName_market[val]
        return val
    
    def translate_groupName_subMarket(self, val):
        if val in Translator.groupName_subMarket:
            return Translator.groupName_subMarket[val]
        return val