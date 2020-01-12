import socket as sc
import threading
from _thread import *
import random
import logging as log
from G_server import G_server
import pickle

def send_pickle(data):
    clientsocket.send(pickle.dumps(data))
def recv_pickle():
    return pickle.loads(clientsocket.recv(2048))


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


global current_player
log.basicConfig(filename="server.log", level=log.DEBUG)
k = G_server()
server = "192.168.1.45"
port = 8000
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM, sc.IPPROTO_SCTP)
s.bind((server, port))
s.listen(5)
print("Waiting for a connection")


def threaded_client(clientsocket, player):
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
            k.append(vector)
                  # tutaj go łączy w wektor wektorów

            while True:
                if k.size() == current_players - 1:  # spradza czy wszyscy wysłali
                    break

            send(current_players)
            if player == 0:
                send_pickle(k)
                """for i in range(current_players):
                    for j in range(6):
                        clientsocket.send(k[i][j])  # Nie wiem czy to działą , pcozekać na łukasza"""
            else:
                send("Sprawdzanie wyników")

            if player == 0:
                vector1 =[]
                vector1 = recv_pickle()
                k.fill(vector1)

            k.check1()
            k.check2()
            vector2 = k.create_score()
            """for i in range(current_players):
                for j in range(2):
                    clientsocket.send(k[i][j])"""
            send_pickle(vector2)

            k.clear()
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
