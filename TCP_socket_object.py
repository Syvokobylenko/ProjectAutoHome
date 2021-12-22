class createConnection():
    def __init__(self):
        import socket
        self.socket = socket.socket()

    def startServer(self,port,max_con):
        self.port = port
        self.socket.bind(('',self.port))
        self.socket.listen(max_con)

    def client(self,IP,port):
        self.IP = IP
        self.port = port
        self.connection = self.socket
        self.connection.connect((self.IP, self.port))
        
    def send(self,message,connection=None):
        if connection is None:
            connection = self.connection
        connection.send(message.encode())

    def recieve(self,timeoutms,maxlenght,connection=None):
        if connection is None:
            connection = self.connection
        connection.settimeout(timeoutms)
        try:
            msg = connection.recv(maxlenght).decode()
        except TimeoutError:
            msg = False
        connection.settimeout(None)
        return msg

