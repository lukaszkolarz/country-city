import var
import Game_For_Sever as gm
import random
from Net_For_S import Server

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

serwer = Server()
serwer.socket_open()
while True:
    client , adres = serwer.connection()
    var.current_players +=1
    ID = ID_generate()
    client = gm.ThreadServer(ID,serwer,client,adres)
    client.start()
