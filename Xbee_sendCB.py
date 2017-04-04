import EXbee

kk = EXbee.EXbee('/dev/ttyUSB0',9600)
kk.API = 2
print "Hello from RPi A!"
response = kk.send_tx("Hello from RPi A!","0013A200414FAB4A","02")
if response['Delivery_status'][:2] == "00":
	response = kk.read_rx()
	print "\tFrame sent successfully"
else:
	print "\tFailed to send frame"
		