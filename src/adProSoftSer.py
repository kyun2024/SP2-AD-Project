import RPi.GPIO as GPIO
import time
import socket
import sys

sensor_pin = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN)

button_pin = 5
GPIO.setup(button_pin, GPIO.IN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen(1)
print('Socket Litsen Start!')
connector, addr = s.accept()
data = connector.recv(1024)
cli_data = data.decode('utf-8')

try:
    Bprev_state = 0
    Sprev_state = 0
    sensor_input = 0
    sta = True
    while sta:
        button_input = GPIO.input(button_pin)
        if (button_input != Bprev_state and button_input == 0):
            print("B-state: %d" % button_input)
            print("Button is clicked!")
            resp  = "Button is clicked!"
            connector.send(resp.encode('utf-8'))
            sta = False
            while True:
                sensor_input = GPIO.input(sensor_pin)
                if (sensor_input != Sprev_state):
                    print("S-state: %d" % sensor_input)
                    if sensor_input == 1:
                        time.sleep(0.1)
                        resp = "goal!"
                        connector.send(resp.encode('utf-8'))
                        sensor_input = GPIO.input(sensor_pin)
                Sprev_state = sensor_input
        Bprev_state = button_input

except KeyboardInterrupt:
    print("Bye!")
    GPIO.cleanup()
