#This is the main file of this program 

import tables
tables.tables()
import pwinput as pp #install pwinput lib using "pip3 install pwinput" statement 
import mainmenu as m1
import mysql.connector as sqltor
import acc_create
import config
import acc_login
import time

#establishing the connection to mysql server backend
mycon = sqltor.connect(
    host = 'localhost',
    user = config.mysql_user,
    passwd = config.mysql_passwd,
    database = 'bank'
)
#Checking if connecter or not
if mycon.is_connected() == False:
   print('Could not connect to database...')

#Creating a sql cursor   
cur = mycon.cursor()

#Run the command below(JUST ONCE) if you do not have any sample data in your table to run the program on
#tables.sample_data()

ch = ''

while ch.lower() != 'exit':
    #Extracting all account numbers from the database into a list
    cur.execute("select AccNo from data")
    acc_data = cur.fetchall()
    allacc_no = []
    for a in acc_data:
        allacc_no.append(a[0])
    #print(allacc_no)
    m1.menu()
    if m1.num == '1':
        acc_create.acc_create()

    elif m1.num == '2':
        acc_login.acc_login()

    elif m1.num.lower() == 'exit':
        time.sleep(0.1)
        m1.leq()
        time.sleep(0.1)
        print("Thank you for using the program!")
        time.sleep(0.1)
        m1.leq()
        break

    else:
        time.sleep(0.1)
        print("Please enter correct option!")
