import network

sta = network.WLAN(network.STA_IF)
sta.active(True)
print(sta.isconnected())
print(sta.scan())