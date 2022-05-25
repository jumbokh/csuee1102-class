import xtools, utime

xtools.connect_wifi_led()

ADAFRUIT_IO_USERNAME = "hueyanchen2014"
ADAFRUIT_IO_KEY = "<AIO KEY>"
FEED1 = "temperature"
FEED2 = "humidity"

while True:
    temp = xtools.random_in_range(10, 35)
    hum = xtools.random_in_range(60, 90)
    print("儲存溫度和濕度資料: ", temp, hum)
    url = "https://io.adafruit.com/api/v2/" + ADAFRUIT_IO_USERNAME
    url+= "/feeds/"+ FEED1 + "/data?X-AIO-Key=" + ADAFRUIT_IO_KEY
    print('url1=', url)
    data1 = {"value": temp}
    xtools.webhook_post(url, data1)
    url = "https://io.adafruit.com/api/v2/" + ADAFRUIT_IO_USERNAME
    url+= "/feeds/"+ FEED2 + "/data?X-AIO-Key=" + ADAFRUIT_IO_KEY
    print('url2=', url)
    data2 = {"value": hum}
    xtools.webhook_post(url, data2)        
    utime.sleep(5)
