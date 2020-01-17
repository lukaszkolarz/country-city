from tkinter import *
import tkinter.ttk as ttk  # widget


class Window(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(500, 500)
        self.master.minsize(600, 600)
        self.master.title("Countries-cities IP")
        self.pack(fill=BOTH, expand=True)

        self.ip_in()

    def ip_in(self):
        global title
        title = ttk.Label(self, text="Countries-cities")
        title.place(x=0, y=30)

        global quest
        quest = ttk.Label(self, text="Insert server IP")
        quest.place(x=10, y=100)

        global e1
        e1 = Entry(self, font="Arial 10 bold")
        e1.place(x=10, y=140, width=320)

        Button(self, text='Submit', command=self.get_ip).place(x=20, y=360)

    def get_ip(self):
        self.ip = e1.get()
        print(self.ip)              #will be deleted
        self.log_in()

    def log_in(self):
        title.destroy()
        quest.destroy()
        e1.destroy()

        global question2
        quest2 = ttk.Label(self, text="Insert your nick")
        quest2.place(x=10, y=100)

        global e2
        e2 = Entry(self, font="Arial 10 bold")
        e2.place(x=10, y=140, width=320)

        Button(self, text='Submit', command=self.get_nick).place(x=20, y=360)

    def get_nick(self):
        self.nick = e2.get()
        print(self.nick)
