import sqlite3


#Craating a database with the customized name if not exist
def connect_to_database():
    conn = sqlite3.connect('Metro_Card_data.db')
    return conn

#Creating a table with the required rows if not exist
def create_table(conn):
    conn=connect_to_database()
    cursor = conn.cursor()
    table_name = 'metro_users'
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()

    if result:
        display_table()
    else:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE metro_users (
                            fname VARCHAR,
                            aadharno INTEGER UNIQUE,
                            metroid INTEGER UNIQUE PRIMARY KEY,
                            balance INTEGER,
                            station VARCHAR
                        )''')
    conn.commit()
    conn.close()

#Closing the connection
def close_connection(conn):
    conn.close()

#Inserting New Passanger Details to Table metro_users
def add_data(name,aadhar_id,card_num,bal):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO metro_users VALUES(?,?,?,?,?)',(name,aadhar_id,card_num,bal,None))
    conn.commit()
    close_connection(conn)


#Displays the existing table- metro_users data
def display_table():
    conn = sqlite3.connect('Metro_Card_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM metro_users")
    rows = cursor.fetchall()
    if(len(rows)>0):
        for row in rows:
            print(row)
    else:
        print("Table 'your_table' does not exist.")

    conn.close()
#display_table()

#retriving the balance for the particular passanger from the database
def retrieve_bal(metro_card_num):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM metro_users where metroid=?', (metro_card_num,))
    bal = cursor.fetchone()
    return bal[0]

#Updating the boarding station name from None to specific station
def update_boarding_sta(source_name,metro_card_num):
    conn=connect_to_database()
    cursor= conn.cursor()
    cursor.execute('UPDATE metro_users SET station= ? WHERE metroid=?',(source_name,metro_card_num) )
    conn.commit()
    close_connection(conn)

#Retrieving the boarding station details and returing the station name where he boarded the metro
def retrieve_boarding_sta(metro_card_num):
    conn=connect_to_database()
    cursor= conn.cursor()
    cursor.execute(' SELECT station FROM metro_users where metroid=?',(metro_card_num,))
    result=cursor.fetchone()
    conn.commit()
    close_connection(conn)
    return result[0]



#Updating the Balance to database for particular Passanger
def bal_update(bal,metro_card_num):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('UPDATE metro_users SET balance= ? WHERE metroid=?',(bal,metro_card_num) )
    conn.commit()
    close_connection(conn)


#Deleting the Table if required
def delete_table(conn):
    conn = sqlite3.connect('Metro_Card_data.db')
    cursor=conn.cursor()
    cursor.execute("DROP TABLE metro_users")
    conn.commit()
    conn.close()

