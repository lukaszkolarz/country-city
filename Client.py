import socket as sc
import Network as net
import Game as gm
import logging as log


print("Hello, insert server IP:")
ip = "localhost"       #input()

session = gm.Game(ip)

print("\nInsert your nick:")
nick = input()

session.setNick(nick)
session.send(nick)
print(session.recv())

msg = ''

while msg != "no":
    letter = session.recvLetter()
    print(letter + "\n")

    print("Insert your answers:")
    print("country:")
    country = input()
    print("city:")
    city = input()
    print("animal:")
    animal = input()
    print("plant:")
    plant = input()
    print("item:")
    item = input()

    session.buildVector(country, city, animal, plant, item)
    session.sendVector(session.vector)
    log.info("Answers sent")

    if int(session.ID) == 0:
        vector = session.recvCheck()
        log.info("Received to check")
        #checking procedure
        session.sendCheckBack(vector)
        log.info("Sent after checking")
    else:
        print(session.recvNotCheck())
        log.info("Waiting for points")

    points = session.recvPoints()
    log.info("Points received")
    #display points
    print("Your score" + session.findMyPoint(points) + "\n")
    log.info("Player's points received")
    print("Would u like to play again? / \"no\" for not")
    msg = input()

session.end()
