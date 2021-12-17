import explorerhat
from time import sleep

while True:
    voltage = explorerhat.analog.one.read()
    print(voltage)
    sleep(0.5)

