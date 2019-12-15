# RPI에서 서버를 실행합니다.

import RPi.GPIO as GPIO
import time
import socket
import sys

button_pin = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin, GPIO.IN)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',8887))

s.listen(1)

print('Socket Litsen Start!')

connector, addr = s.accept()


data = connector.recv(1024)
cli_data = data.decode('utf-8')


try:
    prev_state = 0
    while True:
        button_input = GPIO.input(button_pin)
        if (button_input != prev_state):
            print("state: %d" % button_input)
            if button_input == 1:
                time.sleep(0.1)
                resp = "응답"
                connector.send(resp.encode('utf-8'))
        prev_state = button_input

except KeyboardInterrupt:
    print("Bye!")
    GPIO.cleanup()



s.close()
