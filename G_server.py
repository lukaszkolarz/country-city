import random
import numpy

class G_server:
    def __init__(self):
        self.vector = []

    def append(self,vector1):
        self.vector.append(vector1)

    def size(self):
        a = numpy.shape(self.vector)
        return a

    def check1(self):
        a = numpy.shape(self.vector)
        for i in range(a[0]):
            self.vector[i][6] = 0
        for i in range(a[0]):
            for j in range(1,6):
                if self.vector[i][j] ==0:              ##sprawdzanie zer
                    self.vector[i][6] =+10
    def check2(self):
        a = numpy.shape(self.vector)
        for i in range(1,6):
            for j in range(a[0]):
                for n in range (a[0]):                  #sprawdzanie powtórzen
                    if j!=n:
                        if self.vector[j][i] == self.vector[j][n]:
                            self.vector[j][6] -=5

    def create_score(self):
        score = []
        a = numpy.shape(self.vector)
        a = a[0]
        for i in range(a):
            score[i][0] = self.vector[i][0]
            score[i][1] = self.vector[i][6]
        return score

    def vecscore(self,player):
        vector = []
        for i in range(player):
            vector[i][0] = self.vector[i][0]
            vector[i][1] = self.ve[i][6]
        return vector

    def clear(self):
        self.vector = []
    def fill(self,vec,player):
        for j in range(player):
            for i in range(6):
                self.vector[player][i] = vec[player][i]
