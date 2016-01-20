# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import json
import requests
import urllib2

import bluetooth._bluetooth as bluez

acceptUUID_01 = "addeaddeaddeaddeaddead0002"
acceptUUID_02 = "addeaddeaddeaddeaddead0010"
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"

	for beacon in returnedList:
		uuid = beacon[18:44]
		answ = beacon[47:48]
		#print temp
		#print "\n"
		#print beacon
		#if uuid == acceptUUID_01 and answ != '0' :
			# uuid
			#print answ	

		#else:
			#print "I don't want you!!!"







