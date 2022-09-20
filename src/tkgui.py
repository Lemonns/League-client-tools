from tkinter import *
from tkinter.ttk import Treeview
from turtle import width
from auto_accept import Auto
from window_controls import WindowController
from tkinter import messagebox
from db_commands import insert


class Gui:
    controller = Auto()
    window_controller = WindowController("D:\Riot Games\Riot Client\RiotClientServices.exe")

    def __init__(self, master_root) -> None:
        self.m = master_root
        self.frame = Frame(master_root)
        self.frame.grid()

        self.account_tree = Treeview(master_root, height=10)
        self.account_tree['columns'] = ("Username","Level","Region","Winrate")
        self.account_tree.column("#0", width=0, stretch=NO)
        self.account_tree.column("Username", width=140, stretch=NO)
        self.account_tree.column("Level", width=140, stretch=NO)
        self.account_tree.column("Region", width=140, stretch=NO)
        self.account_tree.column("Winrate", width=140, stretch=NO)

        self.account_tree.bind('<ButtonRelease-1>', self.select_item)






        self.account_tree.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
        self.account_tree.heading("Username", text="Username")
        self.account_tree.heading("Level", text="Level")
        self.account_tree.heading("Region", text="Region")
        self.account_tree.heading("Winrate", text="Winrate")

        self.account_tree.insert('', 'end', values=('Genadoaus', '242','US','52%'))
        self.account_tree.insert('', 'end', values=('370vmatthew', '90','EUW','50%'))
        self.account_tree.insert('', 'end', values=('porker', '920','EUW','20%'))

        self.add_account_btn = Button(master_root, text="Add Account", command=self.test2, width=10)
        self.add_account_btn.grid(row=1, column=1)
        self.accept_btn = Button(master_root, text="Auto Accept", command=self.controller.gui_compatable, width=10)
        self.quit_btn = Button(master_root, text="Quit", command=self.controller.gui_quit, width=10)
        self.accept_btn.grid(row=1, column=2)
        self.quit_btn.grid(row=2, column=2, pady=5)
        self.login_btn = Button(master_root, text="Login", command=lambda:self.window_controller.user_login("test", "test"), width=10)
        self.login_btn.grid(row=2, column=1, pady=5)

 
    def test2(self):
        top = Toplevel(self.m)
        top.geometry("200x200")
        entry = Entry(top, width= 25)
        entry2 = Entry(top, width= 25)
        enter_btn = Button(top, text="Enter", command= lambda:self.get_values(entry, entry2))
        entry.pack()
        entry2.pack()
        enter_btn.pack()


    def get_values(self, username, password):
        accountUsername = username.get()
        accountPassword = password.get()

        print(accountUsername, accountPassword)
        insert(accountUsername, accountPassword)
        #insert(username, password)

    def test(self):
        messagebox.showinfo("W")
        #def popupwin(self):
        #    top= Toplevel(win)

    def select_item(self, a):
        curItem = self.account_tree.focus()
        values = self.account_tree.item(curItem)
        print(values['values'])
        return values['values']

