from TCP_socket_object import createConnection

def node(con):
    while True:
        pc, pc_IP = con.socket.accept()
        print("New connection:", pc_IP)
        while True:
            try:
                print(con.recieve(None,10,pc))
            except ConnectionResetError:
                print("Connection lost:", pc_IP)
                break

if __name__ == "__main__":
    con = createConnection()
    con.startServer(2198,5)
    import threading
    for x in range(5):
        thread = threading.Thread(target=node, args=(con,))
        thread.daemon = False
        thread.start()