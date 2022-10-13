from tkinter import *
from tkinter.ttk import Treeview
from auto_accept import Auto
from window_controls import WindowController
from tkinter import messagebox, ttk
from db_commands import insert, read_data, start_db, get_login_details, delete


class Gui:
    controller = Auto()

    #                                                path of riot client
    window_controller = WindowController("D:\Riot Games\Riot Client\RiotClientServices.exe") 

    def __init__(self, master_root):

        #Selected account
        self.current_account = None

        self.m = master_root
        self.frame = Frame(master_root)
        self.frame.grid()

        self.account_tree = Treeview(master_root, height=10)
        self.account_tree['columns'] = ("Username", "Summoner Name","Level","Region","Winrate","Rank")
        self.account_tree.column("#0", width=0, stretch=NO)
        self.account_tree.column("Username", width=130, stretch=NO)
        self.account_tree.column("Summoner Name", width=130, stretch=NO)
        self.account_tree.column("Level", width=130, stretch=NO)
        self.account_tree.column("Rank", width=130, stretch=NO)
        self.account_tree.column("Region", width=130, stretch=NO)
        self.account_tree.column("Winrate", width=130, stretch=NO)

        self.account_tree.bind('<ButtonRelease-1>', self.select_item)

        self.account_tree.grid(row=0, column=0, columnspan=8, padx=20, pady=20)
        self.account_tree.heading("Username", text="Username")
        self.account_tree.heading("Summoner Name", text="Summoner Name")
        self.account_tree.heading("Level", text="Level")
        self.account_tree.heading("Rank", text="Rank")
        self.account_tree.heading("Region", text="Region")
        self.account_tree.heading("Winrate", text="Winrate")

        start_db(self.account_tree)

        self.add_account_btn = Button(master_root, text="Add Account", command=self.account_modal, width=10)
        self.add_account_btn.grid(row=1, column=1)

        self.delete_btn = Button(master_root, text="Delete", width=10, command=self.delete_account)
        self.delete_btn.grid(row=1, column=2)

        self.accept_btn = Button(master_root, text="Auto Accept", command=self.controller.gui_compatable, width=10)
        self.quit_btn = Button(master_root, text="Quit", command=self.controller.gui_quit, width=10)
        self.accept_btn.grid(row=1, column=3)
        self.quit_btn.grid(row=1, column=4, pady=5)
        self.login_btn = Button(master_root, text="Login", command=self.login_with_info, width=10)
        self.login_btn.grid(row=1, column=5, pady=5)

    
    #creates modal for user to input account details
    def account_modal(self):
        top = Toplevel(self.m)
        top.geometry("210x230")
        variable = StringVar(top)

        username_label = Label(top, text="Username", font=('Arial', 9))
        username_entry = Entry(top, width= 25)

        password_label = Label(top, text="Password", font=('Arial', 9))
        password_entry = Entry(top, width= 25)

        summoner_label = Label(top, text="Summoner Name", font=('Arial', 9))
        summoner_entry = Entry(top, width= 25)

        region_label = Label(top, text="Region", font=('Arial', 9))
        region_dropdown = ttk.Combobox(top, values=("kr", "na", "euw", "eune", "oce", "jp", "br", "las"))

        enter_btn = Button(top, text="Enter", command= lambda:self.get_values(username_entry, password_entry, 
                            summoner_entry, region_dropdown, top))

        username_label.grid(row=1, padx=20)
        username_entry.grid(row=2, padx=20)

        password_label.grid(row=3)
        password_entry.grid(row=4)

        summoner_label.grid(row=5)
        summoner_entry.grid(row=6)
        
        region_label.grid(row=7)
        region_dropdown.grid(row=8)

        enter_btn.grid(row=9, pady=15)
        

    #retrieves data from account input modal
    def get_values(self, username, password, summoner, region, window):
        account_username = username.get()
        account_password = password.get()
        account_summoner = summoner.get()
        account_region = region.get()

        insert(account_username, account_password, account_summoner, account_region)

        for data in self.account_tree.get_children():
            self.account_tree.delete(data)

        for account in read_data():
            formatted_account = list(account)
            formatted_account.pop(6)
            
            self.account_tree.insert(parent='', index='end', iid=formatted_account, text="", values=(formatted_account), tag="orow")

        self.close_window(window)
        
    #returns whatever table row user clicks and returns the values
    def select_item(self, a):
        curItem = self.account_tree.focus()
        values = self.account_tree.item(curItem)
        return values['values']

    def close_window(self, window):
        window.destroy()

    #gets username and password from db and invokes automatic login
    def login_with_info(self):
        curItem = self.account_tree.focus()
        values = self.account_tree.item(curItem)
        login_details = get_login_details(values['values'][0])

        self.window_controller.user_login(username=login_details[0], password=login_details[1])

    def delete_account(self):
        curItem = self.account_tree.focus()
        values = self.account_tree.item(curItem)
        user = values['values'][0]
        
        delete(user)

        for data in self.account_tree.get_children():
            self.account_tree.delete(data)

        for account in read_data():
            formatted_account = list(account)
            formatted_account.pop(6)
            self.account_tree.insert(parent='', index='end', iid=formatted_account, text="", values=(formatted_account), tag="orow")
