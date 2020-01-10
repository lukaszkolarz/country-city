import socket as sc
from Network import Net
from Game import Game

def Client():
    fields = []
    k = Game()
    n = Net()
    
    print(n.receive())
    x = n.send(input())#podawany login
    print(x) # odebranie wiadomosci konczącej sesje powitalna
    while True:
        try:
            litera = n.receive()
            print("Uzupełnij pola wyrazami zaczynającymi się od :",litera)
            break
            #n.send("Odebrano pokiet")
            #print("Państwo, Miasto , Zwięrze, Roślina, Rzecz")
            #vector = k.fiel()
            #for i in range(5):
                #n.send((vector[i]))

            #k.clear()

        except:
            break


Client()









