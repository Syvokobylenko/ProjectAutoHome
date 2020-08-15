class connection():
    def __init__(self):
        import socket
        self.socket = socket.socket()

    def server(self,port):
        self.port = port
        self.socket.bind(('',self.port))
        self.socket.listen(5)
        self.connection, self.clientIP = self.socket.accept()
        return self

    def client(self,IP,port):
        self.IP = IP
        self.port = port
        self.connection = self.socket
        self.connection.connect((self.IP, self.port))
        return self
        
    def send(self,message):
        self.connection.send(message.encode())

    def recieve(self,timeoutms,maxlenght):
        self.connection.settimeout(timeoutms)
        try:
            msg = self.connection.recv(maxlenght).decode()
        except:
            msg = False
        self.connection.settimeout(None)
        return msg