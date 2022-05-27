import time
import am2320
from machine import I2C, Pin
i2c = I2C(scl=Pin(22), sda=Pin(21))
sensor = am2320.AM2320(i2c)

while True:
    sensor.measure()
    print(sensor.temperature())
    print(sensor.humidity())
    time.sleep_ms(4000)