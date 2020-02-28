import machine
import socket

class switchObject():
 def __init__(self, channel):
  self.pin = machine.Pin(channel, machine.Pin.OUT)

def switch(self, state):
 if state:
  self.pin.on()
 else:
  self.pin.off()

class socketConnection():
 def __init__(self, port):
  self.server = socket.socket()
  self.server.bind(('', port))
  self.server.listen(5)

 def acceptCon(self):
  return self.server.accept()

switchGPIO0 = switchObject(0)
server_instance = socketConnection(2198)

while True: 
 data, addr = server_instance.acceptCon()
 print ('Got connection from' + str(addr))
 while True:
  try:
   switchGPIO0.switch(bool(int(data.recv(1).decode())))
  except:
   print(Exception)
 data.close()
