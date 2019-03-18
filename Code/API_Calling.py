#https://www.dataquest.io/blog/python-api-tutorial/
'''
Test on Python 3 
คู่มือ API ของกรมอุตุฯ ก็ตามนี้นะครับ มีอยู่ 11 API ให้เลือกใช้
http://data.tmd.go.th/api/doc/reference/WeatherToday.pdf
อย่าลืมลงทะเบียนเพื่อขอ uid กับ demokey
http://data.tmd.go.th/api/index1.php
'''

import requests
import json
from pprint import pprint

url =  'http://data.tmd.go.th/api/Station/v1/'
# response เป็น json
querystring = {'uid': 'demo', 'ukey': 'demokey', 'format':'json'}
params = { }
# หรือต้องการ response เป็น XML
# querystring = {'uid': 'demo', 'ukey': 'demokey'}
response = requests.request('GET', url,params=querystring)



data=response.json()  #to extract the detail from response
print(data)

print(type(data))
raw_data = data['Station']
