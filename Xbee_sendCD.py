import EXbee

kk = EXbee.EXbee('/dev/ttyUSB0',9600)
kk.API = 2
addresses = ["",""] #addresses of devices to send to
print "Sent message to RPI B and RPi C"
print "Hello from RPi A!"
print "\nResponses:"
for index in range(len(addresses)):
	response = kk.send_tx("Hello from RPi A!", addresses[index],"02")
	if response['Delivery_status'][:2] == "00":
		response = kk.read_rx()
		print "\n\t%s" %response['DATA']
		print "\taddress%s" %response['SOURCE_ADDRESS_64']
	else:
		print "\tNo response from %s, failed to send frame" %addresses['index'][:2]
		