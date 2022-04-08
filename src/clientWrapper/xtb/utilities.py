



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