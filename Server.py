import socket as sc
import threading
from _thread import *
import random
import logging as log
# from G_server import G_server
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
    a = int(a[0])
    print(a)
    vector3 = []
    vector2 = []
    for i in range(a):
        vector2.append(vector[i][0])
        vector2.append(vector[i][1])
        vector2.append(vector[i][2])
        vector2.append(vector[i][3])
        vector2.append(vector[i][4])
        vector2.append(vector[i][5])
        vector2.append(int(0))
        vector3.append(vector2)
        vector2 = []
    return vector3


def check3(vector):
    a = numpy.shape(vector)
    a = a[0]
    for i in range(a):
        for j in range(1, 6):
            if vector[i][j] != "0":
                vector[i][6] += 10
    return vector


def create_score(vector):
    score = []
    score1 = []
    a = numpy.shape(vector)
    a = a[0]
    for i in range(a):
        score1.append(vector[i][0])
        score1.append(vector[i][6])
        score.append(score1)
        score1 = []
    return score


def check2(vector):
    a = numpy.shape(vector)
    a = a[0]
    for i in range(1, 6):
        for j in range(a):
            for n in range(a):  # sprawdzanie powtórzen
                if j != n:
                    if vector[j][i] == vector[n][i] and vector[j][i] != "0":
                        vector[j][6] -= 5

    return vector


def create_score(vector):
    score = []
    score1 = []
    a = numpy.shape(vector)
    a = a[0]
    for i in range(a):
        score1.append(vector[i][0])
        score1.append(vector[i][6])
        score.append(score1)
        score1 = []
    return score


global Vector
global current_player
log.basicConfig(filename="server.log", level=log.DEBUG)
server = "172.19.127.251"
port = 8000
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM, sc.IPPROTO_SCTP)
s.bind((server, port))
s.listen(5)
print("Waiting for a connection")


def threaded_client(clientsocket, player):
    # global Vector
    send(str(player))  # send(str(player))
    login = recv()  # tutaj powinien odebrac login
    print(login)
    send("Zacznijmy zabawę")  # wysłanie wiadomosci konczącej sesje powitalna

    while True:
        try:
            v = generator()
            send(v)  # wysyłamy liczbę
            print(v)
            vector = recv_pickle()
            log.info(" answers received")
            print(vector)
            Vector = []
            Vector.append(vector)
            print(Vector)  # tutaj go łączy w wektor wektorów
            a = numpy.shape(Vector)

            while True:
                if a[0] == current_players:  # spradza czy wszyscy wysłali
                    break

            if player == 0:
                send_pickle(Vector)
                log.info("Answers of all player was sent to client number 0 ")
            else:
                send("Sprawdzanie wyników")
                log.info("Information sent")

            vector1 = []
            vector1 = recv_pickle()
            log.info("Answers was chcecked and received from player number 0")
            print(vector1)

            a = check1(vector1)
            print(a)
            b = check3(a)
            print(b)
            c = check2(b)
            print(c)

            d = create_score(c)
            print(d)
            send_pickle(d)
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
