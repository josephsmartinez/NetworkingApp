import requests
import urllib

from rfc3986 import builder

# datetime-to-rfc-2822
import datetime
import time
from email import utils
# Keyed-Hashing for Message Authentication
import hmac
import hashlib


nowdt = datetime.datetime.now()
nowtuple = nowdt.timetuple()
nowtimestamp = time.mktime(nowtuple)
print(utils.formatdate(nowtimestamp))

date = utils.formatdate(nowtimestamp)
host = "api.fiu.edu"
uri = "/v1/mac/"
username = "case"
method = "GET"
password = "QzY0Q0EzMkItRjcyQy00QkQwLUI4NEYtRDVBRkJCMERDOEUyCg"
mac = "78:24:af:3a:27:ea"

rfc3986_uri = ""

# Array ( [0] => Fri, 01 Feb 2019 02:32:34 +0000 [1] => GET [2] => api.fiu.edu [3] => /v1/mac/78:24:af:3a:27:ea [4] => method=GET&uri=%2Fv1%2Fmac%2F78%3A24%3Aaf%3A3a%3A27%3Aea ) 
# 591fb57dcc7508ff516cbbe5f41f77392392e8ce

# Implementation of RFC 3986 
rfc3986_uri = builder.URIBuilder().add_query_from([('method', 'GET'), ('uri',uri + mac)]).finalize().unsplit()
print(rfc3986_uri[1:]) # FIXME remove (?) from string 


# implode
arr = date + "\n" + method + "\n" + host + "\n" + uri + "\n" + rfc3986_uri[1:]
print(arr)

# Create the signed message from api key and string to sign
p = hmac.new(password.encode('utf-8'), arr.encode('utf-8'), hashlib.sha1).hexdigest()
print(p)

## HTTPS Request
'''
	url : https://api.fiu.edu/v1/mac/78:24:af:3a:27:ea
			curlopt: 
	  				CURLOPT_USERPWD : 
						case : QzY0Q0EzMkItRjcyQy00QkQwLUI4NEYtRDVBRkJCMERDOEUyCg
					CURLOPT_HTTPHEADER : (
						Date: Fri, 01 Feb 2019 02:32:34 +0000,
					(	Content-Type: application/json
'''

# headers = {'Date': date, 'Content-Type': 'application/json'}

# response = requests.get(
# 'https://api.fiu.edu/v1/mac/78:24:af:3a:27:ea/', 
# headers=headers,
# auth=('case', p,),
# verify=True
# )

headers = {
    'Content-type': 'application/json',
}



# Raw Response Content
# 
response = requests.get('https://api.fiu.edu/v1/mac/78:24:af:3a', 
headers=headers, 
data=date, 
auth=('case', p),
stream=True,
verify=True)




print(response.status_code)
print(response.text)



# class api():
#   def __init__ = (self)
#     username = "case"
#     password = "QzY0Q0EzMkItRjcyQy00QkQwLUI4NEYtRDVBRkJCMERDOEUyCg"
  
#   def get_mac(mac):
