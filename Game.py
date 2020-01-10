import random

class Game:
    def __init__(self):
        self.score = 0
        self.fields =[]

    def correct(self,field):
        for i in range(5):
            if field[i] != 0:
                self.score = + 10

        return self.score

    def fiel(self):
        for i in range(5):                      #wpisywanie z klawiatury rzeczy do listry
            self.fields.append(input())
        return self.fields

    def clear(self):                            #usuwanie rzeczy z listy
        self.fields = []


