import socket as sc
import sys
import logging as log


class Network:
    def __init__(self, IP):
        self.client = sc.socket(sc.AF_INET, sc.SOCK_STREAM, sc.IPPROTO_SCTP)
        self.server = IP
        self.port = 8000
        self.addr = (self.server, self.port)
        self.connect()
        log.basicConfig(filename='client.log', level=log.DEBUG)
        log.info(self.recv() + " on: " + self.server + ":" + str(self.port))
        self.ID = self.getID()
        print("Your ID: " + self.ID)

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            self.client.close()
            log.error("Cannot assign connection!")
            sys.exit()

    def getID(self):
        return self.recv()  # get user ID

    def send(self, data):  # sending to server
        self.client.send(bytes(data, "utf-8"))

    def recv(self):  # receiving from server
        msg = self.client.recv(2048).decode("utf-8")
        return msg

    def end(self):
        client.close()
