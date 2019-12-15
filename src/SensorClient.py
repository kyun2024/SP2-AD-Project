import socket
import sys

HOST = '10.42.0.42'
PORT = 8887

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

user_input = input('Message:')
s.send(user_input.encode('utf-8'))

while True:
    echo = s.recv(1024)
    if not echo:
        break
    print(echo.decode('utf-8'))
    print("---------------------------------")

s.close()
