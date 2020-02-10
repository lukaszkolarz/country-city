import threading
import logging as log
import pickle
import numpy
import random
import var
from threading import Lock
import time
lock = Lock()
score = []
wait1 = 0
main_vector = []
log.basicConfig(filename="server.log", level=log.DEBUG)
class ThreadServer(threading.Thread):

    def __init__(self,number,clients,address):
        threading.Thread. __init__(self)
        self.clientsocket = clients
        self.address = address
        self.number = number

    def run(self):
        global wait1
        global main_vector
        self.send("Connected with server")
        self.send(str(self.number))  # send(str(player))
        print(str(self.number))
        login = self.recv()  # tutaj powinien odebrac login
        print(login)
        self.send("Zacznijmy zabawę")  # wysłanie wiaadomości

        while True:
            try:
                main_vector = []

                if self.number == 0:
                    lock.acquire()
                    var.Letter = self.generator()
                    lock.release()
                    self.send(var.Letter)
                    var.wait =1
                else:
                    while True:

                        if var.wait ==1:
                            self.send(var.Letter)
                            break
                        else:
                            time.sleep(1)
                print(var.Letter)
                vector = self.recv_pickle()
                print(vector)
                main_vector.append(vector)
                while True:
                    a = numpy.shape(main_vector)
                    if a[0] == var.current_players:  # spradza czy wsz yscy wysłali
                        break

                if self.number == 0:
                    self.send_pickle(main_vector)
                    lock.acquire()
                    var.main_vector = self.recv_pickle()
                    lock.release()
                    temp = self.check2(self.check3(self.check1(main_vector)))
                    temp1 = self.create_score(temp)
                    score = temp1
                    wait1 = 1
                else:
                    self.send("Sprawdzanie wyników")
                    while (wait1 == 0):
                        time.sleep(0.5)
                    lock.acquire()
                    temp = self.check2(self.check3(self.check1(main_vector)))
                    temp1 = self.create_score(temp)
                    score = temp1
                    lock.release()
                    #time.sleep(3)
                self.send_pickle(score)
                print(score)
                log.info("Score was sent to clients")
                time.sleep(1)
            except:
                print("Lost connection ")
                self.clientsocket.close()
                var.current_players -= 1
                self.ID_attend(self.number)
                break
    def generator(self):
        marks = "abcdefghijklmnouprstuvwyz"
        k = len(marks) - 1
        generate = random.randint(0, k)
        letter = marks[generate]
        return letter

    def check1(self,vector):
        a = numpy.shape(vector)
        a = int(a[0])
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

    def check3(self,vector):
        a = numpy.shape(vector)
        a = a[0]
        for i in range(a):
            for j in range(1, 6):
                if vector[i][j] != "0":
                    vector[i][6] += 10
        return vector

    def create_score(self,vector):
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

    def check2(self,vector):
        a = numpy.shape(vector)
        a = a[0]
        for i in range(1, 6):
            for j in range(a):
                for n in range(a):  # sprawdzanie powtórzen
                    if j != n:
                        if vector[j][i] == vector[n][i] and vector[j][i] != "0":
                            vector[j][6] -= 5

        return vector


    def ID_attend(self,number):
        var.Player_ID.append(number)
        return var.Player_ID

    def send_pickle(self, data):
        self.clientsocket.send(pickle.dumps(data))
        log.info("Client " + str(self.number) + " information sent[pickle]")

    def recv_pickle(self):
        vector = pickle.loads(self.clientsocket.recv(2048))
        log.info("Client " + str(self.number) + " information received[pickle]")
        return vector

    def send(self, data):
        self.clientsocket.send(bytes(data, "utf-8"))
        log.info("Client " + str(self.number) + " information sent"+ "     " +data)

    def recv(self):
        msg = self.clientsocket.recv(2048).decode("utf-8")
        log.info("Client " + str(self.number) + " information received")
        return msg