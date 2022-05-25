from umqtt.simple import MQTTClient
import utime, xtools

xtools.connect_wifi_led()

HOST = "mqtt.thingspeak.com"
CHANNEL_ID = "1256814"
WRITE_API_KEY = "<WRITE API金鑰>"

topic = "channels/" + CHANNEL_ID + "/publish/" + WRITE_API_KEY

client = MQTTClient(xtools.get_id(), HOST)

while True:
    print("儲存溫度和濕度資料!")
    temp = xtools.random_in_range(10, 35)
    hum = xtools.random_in_range(60, 90)
    print(temp, hum)
    payload = "field1="+str(temp)+"&field2="+str(hum)
    client.connect()
    client.publish(topic, payload)
    client.disconnect()
    utime.sleep(15)