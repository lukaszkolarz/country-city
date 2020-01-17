from tkinter import *
import tkinter.ttk as ttk  # widget


class Gui(ttk.Frame):

    def __init__(self,  master=None):
        ttk.Frame.__init__(self, master)

        self.ID = ""
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

    def setId(self, ID):
        self.ID = 0

    def ip_in(self):
        global title
        title = ttk.Label(self, text="Countries-cities", font="Arial 15 bold")
        title.place(x=0, y=0)

        global quest
        quest = ttk.Label(self, text="Insert server IP")
        quest.place(x=0, y=100)

        global e1
        e1 = Entry(self, font="Arial 10 bold")
        e1.place(x=0, y=200, width=320)

        Button(self, text='Submit', command=self.setIp).place(x=20, y=400)

    def setIp(self):
        self.ip = e1.get()

        print(self.ip)              #will be deleted

        self.log_in()

    def log_in(self):
        quest.destroy()
        e1.destroy()

        global connection
        connection = ttk.Label(self, text="Connected to the server :)")
        connection.place(x=0, y=50)

        global id
        id = ttk.Label(self, text=("Your ID: " + self.ID))
        id.place(x=350, y=0)

        global quest2
        quest2 = ttk.Label(self, text="Insert your nick")
        quest2.place(x=0, y=100)

        global e2
        e2 = Entry(self, font="Arial 10 bold")
        e2.place(x=0, y=140, width=320)

        Button(self, text='Submit', command=self.setNick).place(x=20, y=400)

    def setNick(self):
        self.nick = e2.get()

        print(self.nick)            # will be destroy

        self.game()

    def game(self, sign="A"):
        connection.destroy()
        id.destroy()
        title.destroy()
        e2.destroy()
        quest2.destroy()

        global letter
        letter = ttk.Label(self, text=sign, font="Arial 30 bold")
        letter.place(x=400, y=10)

        global quest3
        quest3 = ttk.Label(self, text="Insert your answers")
        quest3.place(x=0, y=20)

        global country_label
        country_label = ttk.Label(self, text="Country:", font="Arial 10")
        country_label.place(x=0, y=50)
        global country
        country = Entry(self, font="Arial 10")
        country.place(x=0, y=70, width=320)

        global city_label
        city_label = ttk.Label(self, text="City:", font="Arial 10")
        city_label.place(x=0, y=100)
        global city
        city = Entry(self, font="Arial 10")
        city.place(x=0, y=120, width=320)

        global animal_label
        animal_label = ttk.Label(self, text="Animal:", font="Arial 10")
        animal_label.place(x=0, y=150)
        global animal
        animal = Entry(self, font="Arial 10")
        animal.place(x=0, y=170, width=320)

        global plant_label
        plant_label = ttk.Label(self, text="Plant:", font="Arial 10")
        plant_label.place(x=0, y=200)
        global plant
        plant = Entry(self, font="Arial 10")
        plant.place(x=0, y=220, width=320)

        global item_label
        item_label = ttk.Label(self, text="Item:", font="Arial 10")
        item_label.place(x=0, y=250)
        global item
        item = Entry(self, font="Arial 10")
        item.place(x=0, y=270, width=320)

        Button(self, text='Submit', command=self.setAns).place(x=20, y=400)

    def setAns(self):
        self.country = country.get()
        self.city = city.get()
        self.animal = animal.get()
        self.plant = plant.get()
        self.item = item.get()

