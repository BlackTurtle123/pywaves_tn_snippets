import pywaves as pw
import time

pw.setNode('https://apitnetworktest.blackturtle.eu','Turtle Network','l')
block = pw.lastblock()
addr = pw.Address(seed='seeeeeeeeedddddd heeeeeerrrrreeeeeeee')
while True:
    try:
        while block['height'] == pw.lastblock()['height']:
            time.sleep(2)

        block = pw.lastblock()
        print(str(block['generator']))
        print(str(block['height']))
        print(str(addr.sendWaves(pw.Address(address=block['generator']),4200,attachment='Thanks for running a node',txFee=2000000)))
    except:
        time.sleep(2)
        print("except")
