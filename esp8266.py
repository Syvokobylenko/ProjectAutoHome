import socket, machine

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
 f = file.read()
 f = f.split("\n")
 credentials = []
 for line in f:
  credentials.append(line)
 file.close()
 return credentials

do_connect(*credentialsRead("wifi.ini"))

class switchObject():
 def __init__(self, channel):
  self.pin = machine.Pin(channel, machine.Pin.OUT)
  self.state = "1"
  self.switch()
 def switch(self):
  if bool(int(self.state)):
   print("Turning OFF")
   self.pin.on()
   self.state = "0"
   return self.state
  else:
   print("Turning ON")
   self.pin.off()
   self.state = "1"
   return self.state

class socketConnection():
 def __init__(self, port):
  self.server = socket.socket()
  self.server.bind(("", port))
  self.server.listen(1)
 def acceptCon(self):
  return self.server.accept()

server_instance = socketConnection(2198)
GPIO0Handler = switchObject(0)

while True:
 data, addr = server_instance.acceptCon()
 print ("Got connection from" + str(addr))
 data.settimeout(5)
 while True:
  try:
   if not bool(int(data.recv(1).decode())):
    data.send(GPIO0Handler.switch())
    data.close()
  except(ValueError):
   print("Invalid Input")
   data.close()
   break
  except(OSError):
   print("Timed Out")
   data.close()
   break
