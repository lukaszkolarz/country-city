import threading
import logging as log
from Net_For_S import Server
import numpy
import random
import var


class ThreadServer(threading.Thread):

    def __init__(self,number,ser,clients,address):
        threading.Thread. __init__(self)
        self.ser = ser
        self.clients1 = clients
        self.address = address
        self.number = number

    def run(self):
        self.ser.send("Connected with server")
        self.ser.send(str(self.number))  # send(str(player))
        print(str(self.number))
        login = self.ser.recv()  # tutaj powinien odebrac login
        print(login)
        self.ser.send("Zacznijmy zabawę")  # wysłanie wiaadomości

        while True:
            try:
                var.main_vector = []

                if self.number == 0:

                    var.Letter = self.generator()

                self.ser.send(var.Letter)
                print(var.Letter)
                vector = self.ser.recv_pickle()
                print(vector)
                var.main_vector.append(vector)
                a = numpy.shape(var.main_vector)
                while True:
                    if a[0] == var.current_players:  # spradza czy wszyscy wysłali
                        break
                if self.number == 0:
                    print(var.main_vector)
                    self.ser.send_pickle(var.main_vector)
                    var.main_vector = self.ser.recv_pickle()
                    var.wait = 1
                else:
                    while True:
                        if var.wait == 1:
                            break
                var.wait = 0
                temp = self.check2(self.check3(self.check1(var.main_vector)))
                temp1 = self.create_score(temp)
                self.ser.send_pickle(temp1)
                log.info("Score was sent to clients")
            except:
                print("Lost connection ")
                self.clients1.close()
                var.current_players -= 1
                self.ID_attend(self.number)
                break
    def generator(self):
        marks = "abcdefghijklmnouprstuvwyz"
        k = len(marks)
        generate = random.randint(0, k)
        letter = marks[generate]
        return letter

    def check1(self,vector):
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






