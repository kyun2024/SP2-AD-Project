import socket
import sys

HOST = '10.42.0.42'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

user_input = input('Message:')
s.send(user_input.encode('utf-8'))

cnt = 0
point = 0

while True:
    echo = s.recv(1024)
    if not echo:
        break
    msg = echo.decode('utf-8')
    if msg == 'goal!':
        if cnt > 0:
            print("골을 넣었습니다!!!")
            print(cnt, "번째 점수 획득")
            point += 1
        cnt += 1
        print("---------------------------------")

s.close()
