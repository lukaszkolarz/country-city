from tkinter import *
import tkinter.ttk as ttk  # widget
import logging as log
import Game as gm


class Gui(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(500, 500)
        self.master.minsize(600, 600)
        self.master.title("Countries-cities IP")
        self.pack(fill=BOTH, expand=True)
        self.ip = ""
        self.nick = ""
        self.country = ""
        self.city = ""
        self.animal = ""
        self.plant = ""
        self.item = ""

        self.ip_in()

    def ip_in(self):
        title = ttk.Label(self, text="Countries-cities", font="Arial 15 bold")
        title.place(x=0, y=0)

        quest = ttk.Label(self, text="Insert server IP")
        quest.place(x=0, y=100)

        global e1
        e1 = Entry(self, font="Arial 10 bold")
        e1.place(x=0, y=200, width=320)

        b1 = Button(self, text='Submit', command=self.setIp)
        b1.place(x=20, y=400)

    def setIp(self):
        self.ip = e1.get()
        global session
        session = gm.Game(self.ip)
        self.log_in()

    def log_in(self):
        self.destroy()

        connection = ttk.Label(self, text="Connected to the server :)")
        connection.place(x=0, y=50)

        id = ttk.Label(self, text=("Your ID: " + session.ID))
        id.place(x=350, y=0)

        quest2 = ttk.Label(self, text="Insert your nick")
        quest2.place(x=0, y=100)

        global e2
        e2 = Entry(self, font="Arial 10 bold")
        e2.place(x=0, y=140, width=320)

        b2 = Button(self, text='Submit', command=self.setNick)
        b2.place(x=20, y=400)

    def setNick(self):
        self.nick = e2.get()
        session.setNick(self.nick)
        session.send(self.nick)
        print(session.recv())
        self.game()

    def game(self):
        self.destroy()
        sign = session.recvLetter()
        letter = ttk.Label(self, text=sign, font="Arial 30 bold")
        letter.place(x=400, y=10)

        quest3 = ttk.Label(self, text="Insert your answers")
        quest3.place(x=0, y=20)

        country_label = ttk.Label(self, text="Country:", font="Arial 10")
        country_label.place(x=0, y=50)
        global country
        country = Entry(self, font="Arial 10")
        country.place(x=0, y=70, width=320)

        city_label = ttk.Label(self, text="City:", font="Arial 10")
        city_label.place(x=0, y=100)
        global city
        city = Entry(self, font="Arial 10")
        city.place(x=0, y=120, width=320)

        animal_label = ttk.Label(self, text="Animal:", font="Arial 10")
        animal_label.place(x=0, y=150)
        global animal
        animal = Entry(self, font="Arial 10")
        animal.place(x=0, y=170, width=320)

        plant_label = ttk.Label(self, text="Plant:", font="Arial 10")
        plant_label.place(x=0, y=200)
        global plant
        plant = Entry(self, font="Arial 10")
        plant.place(x=0, y=220, width=320)

        item_label = ttk.Label(self, text="Item:", font="Arial 10")
        item_label.place(x=0, y=250)
        global item
        item = Entry(self, font="Arial 10")
        item.place(x=0, y=270, width=320)

        b3 = Button(self, text='Submit', command=self.setAns)
        b3.place(x=20, y=400)

    def setAns(self):
        self.country = country.get()
        self.city = city.get()
        self.animal = animal.get()
        self.plant = plant.get()
        self.item = item.get()
        session.buildVector(self.country, self.city, self.animal, self.plant, self.item)
        session.sendVector(session.vector)
        log.info("Answers sent")
        self.checkAns()

    def checkAns(self):
        self.destroy()
        global vector
        log.info("Received to check")

        if int(session.ID) == 0:
            vector = session.recvCheck()
            log.info("Received to check")
            self.buildForCheck()
        else:
            label = self.recvNotCheck()
            wait = ttk.Label(self, text=label, font="Arial 15 bold")
            wait.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.score()

    def zero(self):
        checking = validate.get()
        x = int(checking[:1])
        y = int(checking[2:])
        vector[x-1][y-1] = '0'
        self.destroy()
        self.buildForCheck()


    def sendAfter(self):
        self.destroy()
        print("sended")
        session.sendCheckBack(vector)
        log.info("Sent after checking")
        self.score()

    def score(self):
        self.destroy()
        points = session.recvPoints()
        log.info("Points received")
        y = 10
        for i in points:
            x = 10
            for j in i:
                check = ttk.Label(self, text=j, font="Arial 10")
                check.place(x=x, y=y)
                x += 70
            y += 40
        selfScore = ttk.Label(self, text="Your score: " + session.findMyPoint(points), font="Arial 10 bold")
        selfScore.place(x=0, y=400)
        log.info("Player's points received")
        question = ttk.Label(self, text="Would you like to play again?", font="Arial 10")
        question.place(x=0, y=430)
        a1 = Button(self, text='Again', command=self.game)
        a1.place(x=200, y=470)
        a2 = Button(self, text='Exit', command=self.exit)
        a2.place(x=400, y=470)

    def destroy(self):
        for widget in self.winfo_children():
            widget.destroy()

    def buildForCheck(self):
        global validate
        x = 70
        y = 40
        for i in range(len(vector[0])):
            column = ttk.Label(self, text=str(i+1), font="Arial 10 bold")
            column.place(x=x, y=0)
            x += 70
        for i in range(len(vector)):
            row = ttk.Label(self, text=str(i+1), font="Arial 10 bold")
            row.place(x=0, y=y)
            y += 40

        y = 40
        for i in vector:
            x = 70
            for j in i:
                check = ttk.Label(self, text=j, font="Arial 10")
                check.place(x=x, y=y)
                x += 70
            y += 40

        info = ttk.Label(self,
                         text="Insert row number, then column number separated by comma without space ex: \'2,3\'")
        info.place(x=0, y=350)
        validate = Entry(self, font="Arial 10")
        validate.place(x=0, y=370, width=320)

        a1 = Button(self, text='Submit', command=self.zero)
        a1.place(x=200, y=450)
        a2 = Button(self, text='Exit', command=self.sendAfter)
        a2.place(x=400, y=450)

    def exit(self):
        session.end()
        self.quit()
        self.destroy()
