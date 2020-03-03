import socket, time

class connection:
 def __init__(self, IP, port):
  self.IP = IP
  self.port = port
  self.startConnection()

 def startConnection(self):
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



while True:
 state = input("Type 0 to use switch: ")
 client_soc = connection("192.168.0.39", 2198)
 client_soc.sendData(state)
 print(client_soc.s.recv(1).decode())
 client_soc.s.close()
