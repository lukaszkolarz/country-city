import Network as net
import logging as log
import pickle


class Game(net.Network):
    def __init__(self, ip):
        net.Network.__init__(self, ip)
        self.score = 0
        self.nick = ''
        self.vector = []
        self.letter = ''
        self.playersCount = 0
        self.check = []

    def sendVector(self, vector):
        self.send_pickle(vector)
        log.info(vector[0] + " answers sent")

    def buildVector(self, country, city, animal, plant, item):
        self.vector = [self.nick, country, city, animal, plant, item]

    def setNick(self, nick):
        self.nick = nick

    def recvLetter(self):
        self.letter = self.recv()
        return self.letter

    def recvCheck(self):
        vector = self.recv_pickle()
        return vector

    def sendCheckBack(self, vector):
        self.send_pickle(vector)

    def recvPoints(self):
        points = self.recv_pickle()
        return points

    def checkAnswers(self, positionX, positionY):
        self.check[positionX][positionY] = 0

    def findMyPoint(self, points):
        for i in points:
            if i[0] == self.nick:
                self.score += i[1]
                return str(self.score)
        log.info("No score available!")
        return "Error"
