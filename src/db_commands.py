import sqlite3
from web_fetcher import get_stats


def insert(username, password, summoner, region):
    conn = sqlite3.connect("account_data.db")
    cursor = conn.cursor()

    account_info = get_stats(name=summoner, region=region)

    winrate = account_info["winrate"]
    level = account_info["level"]
    rank = account_info["rank"]

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    accounts(username TEXT, summoner TEXT, level TEXT, region TEXT, winrate TEXT, rank TEXT, password TEXT)""")

    cursor.execute("INSERT INTO accounts VALUES ('" + str(username) + "','" + str(summoner) + "','" 
    + str(level) + "','" + str(region) + "','" + str(winrate) + "','" + str(rank) + "','" + str(password) + "')")
    conn.commit()


def read_data():
    conn = sqlite3.connect("account_data.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    accounts(username TEXT, summoner TEXT, level TEXT, region TEXT, winrate TEXT, rank TEXT, password TEXT)""")
    cursor.execute("SELECT * FROM accounts")
    results = cursor.fetchall()
    conn.commit()

    return results



def update_stats():
    conn = sqlite3.connect("account_data.db")
    cursor = conn.cursor()
    values = read_data()

    for stat in values:
        data = get_stats(stat[1], stat[3])
        user = stat[0]
        sq = "UPDATE accounts SET level = '"+ str(data['level']) +"',  winrate = '"+ str(data['winrate']) +"', rank = '"+ str(data['rank']) +"' WHERE username = '"+ str(user) +"'"
        cursor.execute(sq)
        conn.commit()


def start_db(tree):
        update_stats()

        for data in tree.get_children():
            tree.delete(data)

        for account in read_data():
            tree.insert(parent='', index='end', iid=account, text="", values=(account), tag="orow")

def get_login_details(username: str):
    conn = sqlite3.connect("account_data.db")
    cursor = conn.cursor()

    sq = "SELECT username, password FROM accounts WHERE username = '"+ str(username) +"'"
    cursor.execute(sq)
    result = cursor.fetchall()
    return result[0]

def delete(username):
    conn = sqlite3.connect("account_data.db")
    cursor = conn.cursor()
    sq = "DELETE FROM accounts WHERE username = '"+ str(username) +"'"
    cursor.execute(sq)
    conn.commit()