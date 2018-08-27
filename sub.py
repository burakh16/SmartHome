import paho.mqtt.client as paho
from pyA20.gpio import gpio
from pyA20.gpio import port
import time
import dht22
import datetime
import json
PIN = port.PC7
PIN2 = port.PA6
gpio.init()
instance = dht22.DHT22(pin=PIN2)
def on_publish(client, userdata, mid):
  print("mid: "+str(mid))

client = paho.Client()
client.on_publish = on_publish
client.connect("", 1883)
client.loop_start()

while True:
 result = instance.read()
 if result.is_valid():
	print("Last valid input: " + str(datetime.datetime.now()))
	print("Temperature: %.2f C" % result.temperature)
	print("Humidity: %.2f %%" % result.humidity)
	client.publish("", str(result.temperature), qos=1)
	client.publish("", str(result.humidity), qos=1)
	time.sleep(1)
	state = gpio.input(PIN)
	print(state)
