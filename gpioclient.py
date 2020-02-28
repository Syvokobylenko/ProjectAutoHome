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

server = socket.socket()
server.bind(('', 2198))

server.listen(5)

switchCreate = switchObject(12)

while True: 
 data, addr = server.accept()
 print ('Got connection from' + str(addr))
 while True:
  try:
   switchCreate.switch(bool(int(data.recv(1).decode())))
  except:
   print(Exception)
 data.close()
