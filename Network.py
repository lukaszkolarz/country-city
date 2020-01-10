import socket as sc


class Net:
    def __init__(self):
        self.client = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
        self.server = '192.168.1.45'
        self.port = 8104
        self.addr = (self.server,self.port)
        self.ID = self.connect()
        print(self.ID)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()    #połączenie , uzywane przy wywołaniu
        except:
            pass

    def send(self,data):
        self.client.send(str.encode(data))              #wysyłanie do serwara
        return self.client.recv(2048).decode()

    def receive(self):                                     #odbieranie z serwer
        return self.client.recv(2048).decode()



