import pywaves as py

lock_height = 650000
script = 'height >= ' + str(lock_height)

py.setNode('https://privatenode.blackturtle.eu', 'TN', 'L')
py.setMatcher('https://privatematcher.blackturtle.eu')

address = py.Address(
    seed='')

output = address.setScript(script, txFee=100000000)
print(output)

# output from test needs to be : ""u'message': u'Transaction is not allowed by account-script'
test = address.sendWaves(address, 8000, txFee=2000000)
print(test)
