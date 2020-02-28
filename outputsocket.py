import socket

class socketConnection():
 def __init__(self, port):
  self.server = socket.socket()
  self.server.bind(('', port))
  self.server.listen(5)
 def acceptCon(self):
  return self.server.accept()


server_instance = socketConnection(2198)

while True:
 data, addr = server_instance.acceptCon()
 print ("Got connection from" + str(addr))
 while True:
  try:
   print(bool(int(data.recv(1).decode())))
  except(ValueError):
   print("Invalid Input")
   break
 data.close()
