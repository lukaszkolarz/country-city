import socket as sc
import sys
import logging as log


class Network:
    def __init__(self, IP):
        self.client = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        self.client.setsockopt(sc.SOL_SOCKET, sc.SO_REUSEADDR)
        self.server = IP
        self.port = 8108
        self.addr = (self.server, self.port)
        self.connect()
        log.basicConfig(filename='client.log', level=log.DEBUG)
        log.info(self.client.recv(2048).decode("utf-8") + " on: " + self.server + ":" + str(self.port))
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
        return self.client.recv(2048).decode("utf-8")  # get user ID

    def send(self, data, headerSize=10):  # sending to server
        data = f'{len(data):<{headerSize}}' + data
        self.client.send(data)

    def recv(self, headerSize=10):  # receiving from server
        full_msg = ""
        new_msg = True
        while True:
            msg = self.client.recv(16)
            if new_msg:
                msg_len = int(msg[:headerSize])
                new_msg = False

            full_msg += msg.decode("utf-8")

            if len(full_msg) - headerSize == msg_len:
                full_msg = full_msg[headerSize:]
                break
        return full_msg

    def end(self):
        client.close()
