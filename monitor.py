# test BLE Scanning software
# jcs 6/8/2014

import blescan
import sys
import time
import picamera
import requests
import bluetooth._bluetooth as bluez

file_name = "lot_img.jpg"
url = 'http://10.155.62.87:8080/ParkIT-test/rest/ParkITREST/uploadImage'

def take_picture():
	with picamera.PiCamera() as camera:
		camera.capture(file_name)

def upload_image():
	files = {file_name:open(file_name,'rb')}
	payload = {'lot_id':'0'}
	r = requests.post(url,files=files,data=payload)
	return r.text


#def beaconExists(returnedList)
#	for beacon in returnedList


dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

print 'indefinite monitor started'
while True:
	returnedList = blescan.parse_events(sock, 10)
	if returnedList:
		print "Taking picture..."
		take_picture()
		response = upload_image()
		print "Finished uploading"
		print response
	else:
		print "Scanning..."
	
print 'monitor stopped'

