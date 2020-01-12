import socket as sc
import threading
from _thread import *
import random
import logging as log
from G_server import G_server
import pickle

def send_pickle(data):
    clientsocket.send(pickle.dumps(data))

def send(data, headerSize=10):  # sending to server
    data = f'{len(data):<{headerSize}}' + data
    clientsocket.send(data)

def recv(headerSize=10):  # receiving from server
    full_msg = ""
    new_msg = True
    while True:
        msg = clientsocket.recv(16)
        if new_msg:
            msg_len = int(msg[:headerSize])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg) - headerSize == msg_len:
            full_msg = full_msg[headerSize:]
            break
    return full_msg
def generator():
    marks = "abcdefghijklmnouprstuvwyz"
    k = len(marks)
    generate = random.randint(0, k)
    letter = marks[generate]
    return letter
#def send(msg):
 #   msg = f"{len(msg):<{HEADSIZE}}" + msg
  #  clientsocket.send(bytes(msg,"utf-8"))


log.basicConfig(filename="server.log",level=log.DEBUG)
k = G_server()
server = "172.19.127.251"
port = 8108
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
s.bind((server,port))
s.listen(5)
print("Waiting for a connection")

def threaded_client(clientsocket,player):

    send(str(player))  #send(str(player))
    login = recv() #tutaj powinien odebrac login
    print(login)
    send("Zacznijmy zabawę")     # wysłanie wiadomosci konczącej sesje powitalna
    #reply = clientsocket.recv(1024).decode()
    #print(reply)
    while True:
        try:
            v=send(generator())   #wysyłamy liczbę
            print(v)
            vector = pickle.loads((clientsocket.recv(1024)))
            #for i in range(6):
                #vector[i] =recv()
            #k.append(vector)     #tutaj go łączy w wektor wektorów

            while True:
                if k.size() == current_players - 1:     #spradza czy wszyscy wysłali
                    break

            clientsocket.send(bytes(str(current_players),"utf-8"))
            if player ==0:
                for i in range(current_players):
                    for j in range(6):
                        clientsocket.send(bytes(k[i][j],"utf-8"))     #Nie wiem czy to działą , pcozekać na łukasza
            else:
                clientsocket.send(bytes("Trwa sprawdzania wyników","utf-8"))

            if player == 0:
                for i in range(current_players):
                    for j in range(6):
                        m =clientsocket.recv(1024).decode("utf-8")
                        k[i][j] = m

            k.check1()
            k.check2()
            k.create_score()
            for i in range(current_players):
                for j in range(2):
                    clientsocket.send(bytes(k[i][j],"utf-8"))

            k.clear()
        except:

            break
    print("Lost connection ")
    clientsocket.close()

current_players = 0
while True:
    clientsocket , address = s.accept()
    print("Connection from :",address)
    log.info("Connected from" + str(address))
    send("Connected with server")
    start_new_thread(threaded_client,(clientsocket,current_players))
    current_players +=1




