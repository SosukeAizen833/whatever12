# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from paho.mqtt import client as mqtt_client
import random
import time

broker = 'broker.emqx.io'
port = 1883
topic = '/python/mqtt'
client_id = f"python-mqtt-{random.randint(0,1000)}"
username = 'emqx'
password = 'public'

def connect_mqtt():
    def on_connect(client,userdata,flags,rc):
        if rc == 0:
            print (f"connected to MQTT broker")
        else:
            print(f"failed to connect")
    client = mqtt_client.Client()
    client.username_pw_set(username,password)
    client.on_connect = on_connect
    client.connect(broker,topic)
    return connect

def p