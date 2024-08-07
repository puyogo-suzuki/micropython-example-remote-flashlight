from machine import Pin 
from time import sleep_ms
import network
import socket

ap = network.WLAN(network.AP_IF) # アクセスポイントインタフェースを作成
ap.config(ssid='ESP-AP', authmode=3, password='espespesp') # アクセスポイントの SSID を設定
ap.config(max_clients=2) # ネットワークに接続できるクライアント数を設定
# 自分のIPアドレス, ネットマスク, デフォルトゲートウェイ(とりあえず自分のIPアドレスと同じにする), DNSサーバ(どうでも良い)の指定
ap.ifconfig(('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
ap.active(True)         # インタフェースをアクティブ化

listenSocket = socket.socket() #socketを作成
listenSocket.bind(('192.168.0.1', 1000)) # ソケットを特定のIPアドレスとポートに紐付け
listenSocket.listen(5) # 接続の待受を開始

led = Pin(2, Pin.OUT)
conn, addr = listenSocket.accept()
# クライアントと繋がった
print('accepted')
while True:
    data = conn.recv(1) # データ受信できるまで待つ
    led.value(data[0]) # 0か1の値
