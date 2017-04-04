import EXbee

kk = EXbee.EXbee('/dev/ttyUSB0',9600)
kk.API = 2
addresses = ["","",""] #addresses of devices included in the range test
devices = [] #empty list to store devices in range
print "Message sent: Hello from RPi 1.\n Range test ..."
index2 = 0
for index in range(len(addresses)):
	response = kk.send_tx("Hello, from RPi 1. Range test...", addresses[index],"02")
	if response['Delivery_status'][:2] == "00":
		devices.extend([" "]*1)
		devices[index2] = addresses[index]
		index2 = index2 + 1
		print "\tDiscovery status: %s" %response['Discovery_status'][:2]
		print "\tFrame sent successfully %s\n" %addresses[index]
	    if response['Discovery_status][:2] == "02":
			print "\tRouting protocol was used to send frame\n"
	else:
		print "\tDelivery status: %s" %response[Delivery_status'][:2]
		print "\tFailed to send frame to %s, device not in range\n" %addresses[index]
print "\nDevices in range:"
for index2 in range(len(devices)):
		print "\t%s" %devices[index2]
