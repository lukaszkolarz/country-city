import var
import Game_For_Sever as gm
import random
import socket as sc
import logging as log

log.basicConfig(filename="server.log", level=log.DEBUG)

def ID_generate ():

    if 0 in var.Player_ID:
        ID = 0
        ID_INDEX = var.Player_ID.index(0)
        var.Player_ID.pop(ID_INDEX)
        return ID
    else:
        k = len(var.Player_ID) - 1
        generate = random.randint(0,k)
        ID = var.Player_ID[generate]
        ID_INDEX = var.Player_ID.index(ID)
        var.Player_ID.pop(ID_INDEX)
        return ID

var.Player_ID = [0,1,2,3,4]
var.current_players = 0

server = "localhost"
port = 8000
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM, sc.IPPROTO_SCTP)
s.bind((server,port))
s.listen(5)
while True:
    client , address = s.accept()
    print("Connection from :", address)
    log.info("Connected from" + str(address))
    var.current_players +=1
    ID = ID_generate()
    client = gm.ThreadServer(ID,client,address)
    client.start()
