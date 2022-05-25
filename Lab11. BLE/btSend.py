from machine import Pin
import os
import bluetooth
bt = bluetooth.Bluetooth()
bt.active(1)
bt.advertise(100, 'ESP32_BLE_01')

LED=Pin(2, Pin.OUT) #port 2 is used for led
LED.value(0)

tx = bluetooth.Characteristic('6E400002-B5A3-F393-E0A9-E50E24DCCA9E', bluetooth.FLAG_READ|bluetooth.FLAG_NOTIFY)
rx = bluetooth.Characteristic('6E400003-B5A3-F393-E0A9-E50E24DCCA9E', bluetooth.FLAG_WRITE)
s = bt.add_service('6E400001-B5A3-F393-E0A9-E50E24DCCA9E', [tx, rx])

def callback(char, data):
    print("Get command:",data)
    if(data == b'10'):      
      LED.value(0)
      print("LED OFF")
      tx.write("LED is OFF Now!\n\r")
    if(data == b'11'):
      LED.value(1)
      print("LED ON")
      tx.write("LED is ON Now!\n\r")
    
rx.on_update(callback)