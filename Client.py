import socket as sc
import Network as net
import Game as gm


print("Hello, insert server IP:")
ip = "192.168.1.45"       #input()

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

    if session.ID == 0:
        vector = session.recvCheck()
        #checking procedure
        session.sendCheckBack(vector)
    else:
        session.recvNotCheck()

    points = session.recvPoints()
    #display points
    print("Your score" + session.findMyPoint() + "\n")
    print("Would u like to play again? / \"no\" for not")
    msg = input()

session.end()
