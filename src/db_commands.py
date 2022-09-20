import sqlite3

def insert (username, password):
    conn = sqlite3.connect("account_data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    accounts(username TEXT, password TEXT)""")

    cursor.execute("INSERT INTO accounts VALUES ('" + str(username) + "','" + str(password) + "')")
    conn.commit()


#def insert (username, password, level, region, winrate):
#    conn = sqlite3.connect("account_data.db")
#    cursor = conn.cursor()
#
#    cursor.execute("""CREATE TABLE IF NOT EXISTS 
#    accounts(username TEXT, password TEXT, level TEXT, region TEXT, winrate TEXT)""")
#
#    cursor.execute("INSERT INTO accounts VALUES ('" + str(username) + "','" + str(password) + "','" 
#    + str(level) + "','" + str(winrate) + "','" + str(region) + "')")
#    conn.commit()