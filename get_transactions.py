import pywaves as pw

#configuration
amountAssetID = 'WAVES'
priceAssetID = 'BTC'
traders = ["3Jjp6T5b7T7fWZt8RWEBz4stoGyQrXVWC1r", "3Jz42v5L6pZtUz8nbcVKBroBmZmPL5JnEFt"]

pw.setNode('https://privatenode2.blackturtle.eu', 'turtlenetwork','L')
pw.setMatcher('ttps://privatematcher.blackturtle.eu')
pw.setDatafeed('https://bot.blackturtle.eu')
PAIR = pw.AssetPair(pw.Asset(amountAssetID), pw.Asset(priceAssetID))

#Reward1: Count number of transactions for wallets in trader[] within the last 24 hours for the configured PAIR
#Reward2: Same as Reward1 with an extra check if the amount was > 1
#Reward3: Same as 1 but over a 7 day period

#determine timestamps - 24h
from datetime import datetime
from datetime import timedelta
today = datetime.today()
yesterday = today - timedelta(days=1)
lastweek = today - timedelta(days=7)

today = int(round(datetime.timestamp(today) * 1000))
yesterday = int(round(datetime.timestamp(yesterday) * 1000))
lastweek = int(round(datetime.timestamp(lastweek) * 1000))

#print("today =", today)
#print("yesterday =", yesterday)

#create traders list
traderdictR1 = {}
traderdictR2 = {}
traderdictR3 = {}

for tr in traders:
    traderdictR1[tr] = "0"
    traderdictR2[tr] = "0"
    traderdictR3[tr] = "0"
    
#print(traderdict)

#get trades last 24 hrs
trades = PAIR.trades(yesterday, today)
for t in trades:
    #Reward1 Check
    if t['buyer'] in traderdictR1:
        traderdictR1[t['buyer']] = str(int(traderdictR1[t['buyer']]) + 1)
        #Reward2 check
        if float(t['amount']) > 1:
            traderdictR2[t['buyer']] = str(int(traderdictR2[t['buyer']]) + 1)

    if t['seller'] in traderdictR1:
        traderdictR1[t['seller']] = str(int(traderdictR1[t['seller']]) + 1)
        #Reward2 check
        if float(t['amount']) > 1:
            traderdictR2[t['seller']] = str(int(traderdictR2[t['seller']]) + 1)

#get trades last 7 days
trades = PAIR.trades(lastweek, today)
for t in trades:
    #Reward3 Check
    if t['buyer'] in traderdictR3:
        traderdictR3[t['buyer']] = str(int(traderdictR3[t['buyer']]) + 1)

    if t['seller'] in traderdictR3:
        traderdictR3[t['seller']] = str(int(traderdictR3[t['seller']]) + 1)
        

#print(t)
    
print("Traders for Reward 1")
print(traderdictR1)
print("Traders for Reward 2")
print(traderdictR2)
print("Traders for Reward 3")
print(traderdictR3)
