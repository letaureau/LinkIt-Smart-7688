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
    link = "https://jawbone.com/nudge/api/users/@me/sleeps?"
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
        times = json.dumps(items[item]["details"]["awake_time"])
        times = float(times)
        times = formatting(times)
        times2 = json.dumps(items[item]["details"]["asleep_time"])
        times2 = float(times2)
        times2 = formatting(times2)
        times4 = strptime(times2, '%Y,%m,%d,%H,%M,%S')
        times3 = strptime(times, '%Y,%m,%d,%H,%M,%S')
        times3 = datetime.datetime(*times3[:6])
        times4 = datetime.datetime(*times4[:6])
        print("Went to Bed : ")
#        myLcd.setCursor(0,0)
        #time.sleep(5)
#        myLcd.setCursor(1,0)
        print(times2)
        time.sleep(5)
#        myLcd.clear()
#        myLcd.setCursor(0,0)
        print("Got UP  : ")
        #time.sleep(5)
#        myLcd.setCursor(1,0)
        print(times)
        time.sleep(5)
#        myLcd.clear()
        #myLcd.setCursor(1,0)
        #time.sleep(5)
        #print "asleep time : ", times4
        #print "awake time  : ", times3
        uptime = times3 - times4
        uptime2 = str(uptime)
#        myLcd.setCursor(0,0)
        print("sleep hours :")
#        myLcd.setCursor(1,0)
        print(uptime2)
        #print "asleep hours :", uptime2  # uptime.total_seconds()," seconds"
#        myLcd.setCursor(1,7)
        if (uptime.total_seconds() >= 22000):
            print("GOOD SLEEP")
            time.sleep(5)
#            myLcd.clear()
        else:
            print("BAD SLEEP")
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
