import socket as sc
import threading
from _thread import *
import random
def generator():
    marks = "abcdefghijklmnouprstuvwyz"
    k = len(marks)
    generate = random.randint(0, k)
    letter = marks[generate]
    return letter
server = "172.19.127.251"
port = 8107
s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
s.bind((server,port))
s.listen(5)
print("Waiting for a connection")


def threaded_client(clientsocket, player):

    clientsocket.send(str.encode("    Connected Jaki masz login"))
    login = clientsocket.recv(1024) #tutaj powinien odebrac login
    reply = login.decode("utf-8")
    print(reply)
    clientsocket.send(str.encode("Zacznijmy zabawe")) # wysłanie wiadomosci konczącej sesje powitalna
    while True:
        try:
            #print(clientsocket.recv(1024).decode("utf-8"))
            clientsocket.send(str.encode( generator()))    #wysyłamy liczbę
            print(clientsocket.recv(1024).decode("utf-8"))

            vector = []
            for i in range(5):
                vector[i]=clientsocket.recv(1024).decode("utf-8")
                print(clientsocket.send(str.encode(("wektor odebrany"))))
            print(vector)



            if not login:
                break
            else:
                print("Received:", reply)
                print("Sending",reply)

            clientsocket.sendall(str.encode(reply))
        except:
            break
    print("Lost connection ")
    clientsocket.close()

current_players = 0
while True:
    clientsocket , address = s.accept()
    print("Connection from :",address)
    clientsocket.send(bytes("Connected with server","utf-8"))
    start_new_thread(threaded_client,(clientsocket,current_players))
    current_players +=1




