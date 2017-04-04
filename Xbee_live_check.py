import EXbee

kk = EXbee.EXbee('/dev/ttyUSB0',9600)
kk.API = 2
addresses = ["","",""] #addresses of devices ping
devices = [] #empty list to store available devices
print "Message sent: Hello from RPi 2.\n Looking for devices ..."
index2 = 0
for index in range(len(addresses)):
	response = kk.send_tx("Hello, from RPi 2", addresses[index],"02")
	if response['Delivery_status'][:2] == "00":
		devices.extend([" "]*1)
		devices[index2] = addresses[index]
		index2 = index2 + 1
		print "\tDiscovery status: %s" %response['Discovery_status'][:2]
		print "\tFrame sent successfully %s\n" %addresses[index]
	elif response['Discovery_status][:2] == "02":
		print "\tSearching for route.."
	else:
		print "\tDelivery status: %s" %response[Delivery_status'][:2]
		print "\tFailed to send frame to %s, device not available\n" %addresses[index]
print "\nAvailable devices:"
for index in range(len(devices)):
		print "\t%s" %devices[index]
