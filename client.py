from machine import Pin 
from time import sleep_ms
import network
import socket
# WiFiを有効にする 
wlan = network.WLAN(network.STA_IF) 
wlan.active(True) 
# 基地局に接続 
wlan.connect('ESP-AP', 'espespesp') 
# アドレスの確認 
print(wlan.ifconfig())

s = socket.socket() #ソケットの作成
host = '192.168.0.1' #接続先のipアドレス
port = 1000 #ポート指定

s.connect(socket.getaddrinfo(host, port)[0][-1]) #接続確立
print('connected')
button = Pin(4, Pin.IN, Pin.PULL_UP)
led = 0
btn = button.value()
while True:
    btnp = btn
    btn = button.value()
    # ボタンが押された
    if btnp == 0 and btn == 1:
        # LEDを反転する
        led = 0 if led == 1 else 1
        # 0/1をサーバ側に送信する
        s.send(bytes([led]))
    sleep_ms(1)
