import socket, machine

class switchObject():
 def __init__(self, channel):
  self.pin = machine.Pin(channel, machine.Pin.OUT)

 def switch(self, state):
  if state:
   print("Turning ON")
   self.pin.on()
  else:
   print("Turning OFF")
   self.pin.off()

class socketConnection():
 def __init__(self, port):
  self.server = socket.socket()
  self.server.bind(('', port))
  self.server.listen(5)
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
   GPIO0Handler.switch(bool(int(data.recv(1).decode())))
  except(ValueError):
   print("Invalid Input")
   break
  except(socket.timeout):
   print("Timed Out")
   data.close()
   break
 data.close()
