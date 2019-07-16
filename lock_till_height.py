import pywaves as py

lock_height = 650000
script = 'height >= '+str(lock_height)

py.setNode('http://localhost:6861', 'TN', 'L')
py.setMatcher('https://privatematcher.blackturtle.eu')


address = py.Address(seed='')

output = address.setScript(script,txFee=100000000)
print(output)
