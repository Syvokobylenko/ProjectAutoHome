import read_file, TCP_socket_object, wifi_connect, machine, time

ipconfig = wifi_connect.do_connect(*read_file.credentialsRead("wifi.ini"))
con = TCP_socket_object.createConnection()
con.client(ipconfig[3],2198)

pin = machine.Pin(0, machine.Pin.IN)

while True:
    if not pin.value():
        con.send('1')
        time.sleep(2)
