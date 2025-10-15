import time
import hashlib
import hmac
import base64
import urllib.request
from bs4 import BeautifulSoup

partner_id = 'public'                      # ID provided by AB. 
partner_key = '2jfaWErgt2+o48gsk302kd'     # Key provided by AB.
partner_id = 'gmenyhertapi'                      # ID provided by AB. 
partner_key = '9KwHOlQDPzgCMYdoDoSp4g'     # Key provided by AB.
expires = str(int(time.time() + 86400))    # Seconds since epoch. Example expires in 24 hours.
user_id = '383485'                         # Partner defined. May be an empty string.

message = expires + "\n" + user_id
digest = hmac.new(partner_key.encode(), message.encode(), digestmod=hashlib.sha256).digest()
signature = base64.b64encode(digest).decode()
encoded_sig = urllib.parse.quote_plus(signature)
parms = 'partner.id=' + partner_id + \
        '&auth.signature=' + encoded_sig + \
        '&auth.expires=' + expires + \
        '&user.id=' + user_id
result = urllib.request.urlopen('https://canvas.asu.edu/courses/240102/assignments/6781491#' + parms).read()

out_file = open('output.txt', 'w')

print (result, file=out_file)

parsed_result = BeautifulSoup(result,'html')

print(parsed_result.body.find('div'))

out_file.close()