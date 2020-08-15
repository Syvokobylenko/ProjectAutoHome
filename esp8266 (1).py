import gpio, read_file, TCP_socket_object, wifi_connect
wifi_connect.do_connect(*read_file.credentialsRead("wifi.ini"))

GPIO0Handler = gpio.switchObject(0)

while True:
 data, addr = TCP_socket_object.server(2198)
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
