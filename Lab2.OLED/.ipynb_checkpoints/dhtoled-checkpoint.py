import machine, dht, utime,ssd1306
d11=dht.DHT11(machine.Pin(15))
hw_i2c1 = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))# machine.I2C(0x3c, freq=200000)        
oled096=ssd1306.SSD1306_I2C(128, 64, hw_i2c1)
oled096.fill(0) 
oled096.text('~ TEMP & HUMID ~',0,0)
oled096.text('Temp =    C',0,16)
oled096.text('Humid=    %',0,32)
oled096.show()
try:
    while 1:
        utime.sleep_ms(2000)
        d11.measure()
        oled096.fill(0)     
        oled096.text('~ TEMP & HUMID ~',0,0) 
        oled096.text('Temp = {} C'.format(d11.temperature()),0,16)
        oled096.text('Humid= {} %'.format(d11.humidity()),0,32)
        oled096.show()
        print('today temp ={}, humidity= {}'.format(d11.temperature(),d11.humidity()))
except Exception as e: print(e)