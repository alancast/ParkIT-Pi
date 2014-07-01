import requests

print 'START'
url = 'http://10.155.69.194:8080/ParkIT-test/rest/ParkITREST/uploadImage'
files = {'lot_img.jpg':open('./lot_img.jpg', 'rb')}
payload = {'lot_id':'1'}
r = requests.post(url,files=files,data=payload)
print r.text
print 'END'
