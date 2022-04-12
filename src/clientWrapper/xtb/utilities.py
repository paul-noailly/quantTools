import datetime



# Command templates
def baseCommand(commandName, arguments=None):
    if arguments==None:
        arguments = dict()
    return dict([('command', commandName), ('arguments', arguments)])

def loginCommand(userId, password, appName=''):
    return baseCommand('login', dict(userId=userId, password=password, appName=appName))


# streaming printer: function that print the message comming from the socket stream

# example function for processing ticks from Streaming socket
def procTickMsgPrinter(msg): 
    print("TICK: ", msg)

# example function for processing trades from Streaming socket
def procTradeMsgPrinter(msg): 
    print("TRADE: ", msg)

# example function for processing trades from Streaming socket
def procBalanceMsgPrinter(msg): 
    print("BALANCE: ", msg)

# example function for processing trades from Streaming socket
def procTradeStatusMsgPrinter(msg): 
    print("TRADE STATUS: ", msg)

# example function for processing trades from Streaming socket
def procProfitMsgPrinter(msg): 
    print("PROFIT: ", msg)

# example function for processing news from Streaming socket
def procNewsMsgPrinter(msg): 
    print("NEWS: ", msg)
    
    
# months

def get_datetime_previous_month(date:datetime.datetime) -> datetime.datetime:
    previous_month = (date.month-2)%12+1
    previous_year = date.year - previous_month//12
    return datetime.datetime(previous_year, previous_month, date.day)


def get_datetime_next_month(date:datetime.datetime) -> datetime.datetime:
    next_month = date.month%12+1
    next_year = date.year + date.month//12
    return datetime.datetime(next_year, next_month, date.day)
