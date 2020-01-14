import socket as sc
import threading
from _thread import *
import random
import logging as log
#from G_server import G_server
import pickle
import numpy
def send_pickle(data):
    clientsocket.send(pickle.dumps(data))
def recv_pickle():
    vector = pickle.loads(clientsocket.recv(2048))
    log.info(" answers sent")
    return vector
def send(data):  # sending to server
    clientsocket.send(bytes(data, "utf-8"))
def recv():  # receiving from server
    msg = clientsocket.recv(2048).decode("utf-8")
    return msg
def generator():
    marks = "abcdefghijklmnouprstuvwyz"
    k = len(marks)
    generate = random.randint(0, k)
    letter = marks[generate]
    return letter
def check1(vector):
    a = numpy.shape(vector)
    for i in range(a[0]):
        vector[i][6] = 0
    for i in range(a[0]):
        for j in range(1,6):
            if vector[i][j] != 0:
                vector[i][6] =+10
    return vector
def check2(vector):
    a = numpy.shape(vector)
    a = a[0]
    for i in range(1, 6):
        for j in range(a):
            for n in range(a):  # sprawdzanie powtórzen
                if j != n:
                    if vector[j][i] == vector[j][n]:
                        vector[j][6] -= 5

    return vector
def create_score(vector):
    score = []
    a = numpy.shape(vector)
    a = a[0]
    for i in range(a):
        score[i][0] = vector[i][0]
        score[i][1] = vector[i][6]
    return score

global Vector
global current_player
log.basicConfig(filename="server.log", level=log.DEBUG)
#k = G_server()
server = "172.19.127.251"
port = 8000
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM, sc.IPPROTO_SCTP)
s.bind((server, port))
s.listen(5)
print("Waiting for a connection")


def threaded_client(clientsocket, player):
    #global Vector
    send(str(player))  # send(str(player))
    login = recv()  # tutaj powinien odebrac login
    print(login)
    send("Zacznijmy zabawę")     # wysłanie wiadomosci konczącej sesje powitalna

    while True:
        try:
            v = generator()
            send(v)  # wysyłamy liczbę
            print(v)
            vector = []
            vector = recv_pickle()
            log.info(" answers received")
            print(vector)
            Vector = []
            Vector.append(vector)
            print(Vector)      # tutaj go łączy w wektor wektorów
            a = numpy.shape(Vector)

            while True:
                if a[0] == current_players  :  # spradza czy wszyscy wysłali
                    break

            if player == 0:
                send_pickle(Vector)
                log.info("Answers of all player was sent to client number 0 ")
            else:
                send("Sprawdzanie wyników")
                log.info("Information sent")

            if player == 0:
                vector1 =[]
                vector1 = recv_pickle()
                log.info("Answers was chcecked and received from player number 0")

            Vector = check1(vector1)
            Vector = check2(vector1)


            Vector = create_score(Vector)
            """for i in range(current_players):
                for j in range(2):
                    clientsocket.send(k[i][j])"""
            send_pickle(Vector)
            log.info("Score was sent to clients")

            Vector = []
        except:

            break
    print("Lost connection ")
    clientsocket.close()


current_players = 0
while True:
    clientsocket, address = s.accept()
    print("Connection from :", address)
    log.info("Connected from" + str(address))
    send("Connected with server")
    start_new_thread(threaded_client, (clientsocket, current_players))
    current_players += 1
