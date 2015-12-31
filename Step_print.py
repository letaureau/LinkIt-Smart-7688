import sys
import urllib
import urllib2
import json
import datetime
from datetime import timedelta
from time import strptime
#import pyupm_i2clcd as lcd
import time
def formatting(entry):
    t = datetime.datetime.fromtimestamp(float(json.dumps(entry))).strftime('%Y,%m,%d,%H,%M,%S')
    f_entry = str(t)
    return t
# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
while True:
#    myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
#    myLcd.setCursor(0,0)
    user = "user"
    passwd = "password"
    link = "https://jawbone.com/nudge/api/users/@me/moves?"
    url = 'https://jawbone.com/user/signin/login'
    params = urllib.urlencode({
        'email': user,
        'pwd': passwd,
        'service': 'nudge'
        })
    tokenresponse = urllib2.urlopen(url, params)
    data = json.load(tokenresponse)
    token_num = data["token"]
    opener = urllib2.build_opener()
    opener.addheaders.append(('x-nudge-token', token_num))
    dataresponse = opener.open(link)
    data = json.load(dataresponse)
    meta = data['meta']
    data2 = data['data']
    items = data['data']['items']
    size = data['data']['size']
    item = 0
    for item in range(0, size):
        dates = items [item]['date']
        steps = items [item]['title']
#        myLcd.setCursor(0,0)
        print("Dates : ")
#        myLcd.setCursor(1,0)
        print(dates)
        time.sleep(5)
#        myLcd.clear()
#        myLcd.setCursor(0,0)
        print("Total Steps")
#        myLcd.setCursor(1,0)
        print(steps)
#        myLcd.setCursor(1,7)
        if (steps >= 10000):
            print("GOOD MOVE")
            time.sleep(5)
#            myLcd.clear()
        else:
            print("BAD MOVE")
            time.sleep(5)
#            myLcd.clear()
    # RGB Blue
    #myLcd.setColor(53, 39, 249)
    #time.sleep(5)

    # RGB Red
#    myLcd.setColor(255, 0, 0)
#    myLcd.setColor(0,255, 0)
#    myLcd.setColor(0,0,255)

#time.sleep(5)

#print("asleep time : ", times4)
#myLcd.setCursor(1,2)
#print("awake time  : ", times3)
#time.sleep(5)
