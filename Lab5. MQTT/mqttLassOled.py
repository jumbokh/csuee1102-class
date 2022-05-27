from umqtt.simple import MQTTClient
from machine import Pin, ADC, I2C
import ssd1306
import machine,dht,utime,time,network
import config

i2c = I2C(sda=Pin(21), scl=Pin(22))
oled096 = ssd1306.SSD1306_I2C(128, 64, i2c)
oled096.fill(0)
oled096.text('~ TEMP & HUMID ~',0,0)
oled096.text('Temp =    C',0,16)
oled096.text('Humid=    %',0,32)
oled096.text('PM2.5=    %',0,48)
oled096.show()
mq_server = 'broker.emqx.io'
#mq_server = '192.168.1.103'
mq_id = 'esp00001' 
mq_topicT = b'csuclass/lass/T'
mq_topicH = b'csuclass/lass/H'
mq_topicPM25 = b'csuclass/lass/PM25'
mq_user=''
mq_pass=''
SSID = config.SSID        # WiFi名稱
PASSWORD = config.PASSWORD   # WiFi密碼
d11=dht.DHT11(machine.Pin(15))      # GPIO14 as the DHT11 dataline
p0 = Pin(13, Pin.OUT)
adc = ADC(Pin(35))

def measure():
 p0.value(1)                       # d?but du cr?neau
 time.sleep_us(280)         # les 0.28 ms
 readvalue = adc.read()    # lecture de l’adc
 time.sleep_us(40)           # compl?ment du cr?neau ? 0.32 ms
 p0.value(0)                        # fin du cr?neau
 time.sleep_us(9680)        # compl?ment du cycle ? 10 ms
 return readvalue
#--------------------------------------
t=measure()
def getDust():
  t,tot,t1=0,0,0
  ppm=0.0
  for i in range(10):  # on fait 10 mesures
     t=measure()
     tot=tot+t
  ppm=tot/10
  return ppm

wifi= network.WLAN(network.STA_IF)
wifi.active(True)

try:
    #wifi.connect(SSID, PASSWORD)
    print('start to connect wifi')
    for i in range(20):
        print('try to connect wifi in {}s'.format(i))
        utime.sleep(1)
        if wifi.isconnected():
            break          
    if wifi.isconnected():
        print('WiFi connection OK!')
        print('Network Config=',wifi.ifconfig())
    else:
        print('WiFi connection Error')      
    mqClient0 = MQTTClient(mq_id, mq_server, user=mq_user, password=mq_pass)
    mqClient0.connect()
    i=0
    while True:
        d11.measure()
        #mq_message='T={},H={}'.format(d11.temperature(),d11.humidity())
        m1 = d11.temperature()
        m2 = d11.humidity()
        m3 = getDust()
        mqClient0.publish(mq_topicT, str(m1))
        mqClient0.publish(mq_topicH, str(m2))
        mqClient0.publish(mq_topicPM25, str(m3))
        strm1 = 'Temp = '+str(m1)+' C'
        strm2 = 'Humid=  '+str(m2)+'  %'
        strm3 = 'PM2.5=  '+str(m3)+'  %'
        oled096.fill(0)
        oled096.text('~ TEMP & HUMID ~',0,0)
        oled096.text(strm1,0,16)
        oled096.text(strm2,0,32)
        oled096.text(strm3,0,48)
        oled096.show()
        time.sleep(5)
        i=i+1
        print("T={}, H={} PM25={}--> {}".format(m1,m2,m3,i))
        if i>20: break
except Exception as e:
    print('mqtt exception error: ',e)

