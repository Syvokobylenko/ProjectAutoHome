def do_connect(ESSID,password):
 import network
 network.WLAN(network.AP_IF).active(False)
 sta_if = network.WLAN(network.STA_IF)
 if not sta_if.isconnected():
  print("connecting to network...")
  sta_if.active(True)
  sta_if.connect(ESSID, password)
  while not sta_if.isconnected():
   pass
  print("network config:", sta_if.ifconfig())

def credentialsRead(filename):
 file = open(filename,"r")
 f = file.read().split("\n")
 file.close()
 return f

do_connect(*credentialsRead("wifi.ini"))

class connection:
 def __init__(self, IP, port):
  self.IP = IP
  self.port = port
  self.startConnection()

 def startConnection(self):
  import socket
  self.s = socket.socket()
  try:
   self.s.connect((self.IP, self.port))
  except(KeyboardInterrupt):
   exit

 def sendData(self, state):
  try:
   self.s.send(str(state))
  except(KeyboardInterrupt):
   exit

def sendSocket():
 import machine, time
 pinIN = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
 pin_state = pinIN.value()
 while True:
  try:
   if pinIN.value() != pin_state:
    pin_state = pinIN.value()
    client_soc = connection("192.168.0.73", 2198)
    client_soc.sendData("0")
    client_soc.s.recv(1)
    client_soc.s.close()
    time.sleep(2)
  except(ValueError):
   print("Invalid Input")
   client_soc.close()
  except(OSError):
   print("Timed Out")
   client_soc.close()

sendSocket()
