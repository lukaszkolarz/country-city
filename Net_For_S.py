import socket as sc
import sys
import logging as log
import pickle

log.basicConfig(filename="server.log", level=log.DEBUG)

class Server:
    def __init__(self):
        self.server = "172.19.127.251"
        self.port = 8000
        self.s = sc.socket(sc.AF_INET, sc.SOCK_STREAM, sc.IPPROTO_SCTP)

    def socket_open(self):
        self.s.bind((self.server, self.port))
        self.s.listen(5)

    def connection(self):
        clients1 , address = self.s.accept()
        self.clientsocket = clients1
        self.address = address
        print("Connection from :", self.address)
        log.info("Connected from" + str(self.address))
        return self.clientsocket , self.address

    def send_pickle(self,data):
        self.clientsocket.send(pickle.dumps(data))
        log.info("Information sent[pickle]")

    def recv_pickle(self):
        vector = pickle.loads(self.clientsocket.recv(2048))
        log.info(" Information received[pickle]")
        return vector

    def send(self,data):  # sending to server
        self.clientsocket.send(bytes(data, "utf-8"))
        log.info(" Information sent")

    def recv(self):  # receiving from server
        msg = self.clientsocket.recv(2048).decode("utf-8")
        log.info(" Information received")
        return msg

    def end(self):
        self.s.close()
        log.info("Server closed")

