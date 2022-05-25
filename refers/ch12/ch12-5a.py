from umqtt.simple import MQTTClient
import utime, xtools

xtools.connect_wifi_led()

ADAFRUIT_IO_USERNAME = "hueyanchen2014"
ADAFRUIT_IO_KEY = "<AIO KEY>"
FEED1 = "temperature"
FEED2 = "humidity"

# MQTT 客戶端
client = MQTTClient (
    client_id = xtools.get_id(),
    server = "io.adafruit.com",
    user = ADAFRUIT_IO_USERNAME,
    password = ADAFRUIT_IO_KEY,
    ssl = False,
)

topic1 = ADAFRUIT_IO_USERNAME + "/feeds/" +FEED1
topic2 = ADAFRUIT_IO_USERNAME + "/feeds/" +FEED2

while True:
    print("儲存溫度和濕度資料!")
    temp = xtools.random_in_range(10, 35)
    hum = xtools.random_in_range(60, 90)
    print(temp, hum)
    client.connect()
    client.publish(topic1, str(temp))
    utime.sleep(5) 
    client.publish(topic2, str(hum))
    utime.sleep(5)
    client.disconnect()
    utime.sleep(5)