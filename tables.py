#File handles the tables of mysql-server required by this program 

import mysql.connector as sqltor
import config
#establishing the connection
mycon = sqltor.connect(
    host = 'localhost',
    user = config.mysql_user,
    passwd = config.mysql_passwd,
    
)
if mycon.is_connected() == False:
   print('Could not connect to database...')

cur = mycon.cursor()

def tables(): 
    cur.execute("SHOW DATABASES")
    if ("bank",) in cur:
#        print("Database exist")
        cur.reset()
        cur.execute("USE bank")
        mycon.commit()
        
    else:
        print("First Time configuration, Database doesnt exist")
        cur.execute("CREATE DATABASE {}".format("bank"))
        cur.execute("USE bank")
        print("DATABASE CREATED")
        

        table_data = ('''create table data(
                    AccNo int,
                    Name char(30),
                    Phone bigint(20),
                    Age int(3),
                    Address char(70),
                    balance float(20),
                    PRIMARY KEY (AccNo))
                ''')
        cur.execute(table_data)

        table_pass = ('''create table pass(
                    AccNo int,
                    Password varchar(30),
                    FOREIGN KEY (AccNo) REFERENCES data(AccNo))
                ''')
        cur.execute(table_pass)
        table_transactions = ('''create table trans(
                    AccNo int,
                    Time datetime,
                    Transaction char(15),
                    Amount float(20),
                    Remarks char(30),
                    FOREIGN KEY (AccNo) REFERENCES data(AccNo))
                ''')
        cur.execute(table_transactions)
        

def sample_data():
    cur.execute("USE bank")

    data_sample = ("insert into data values(%s, %s, %s, %s, %s, %s)")
    record1 = [(111,'Utkarsh Khichariya',23456789,17,'A-169, BC Nagar, New Delhi',10000),
                (543,'Sonal Jaiswal',873483874,19,'B2-312,Dream Board Colony, Kolkata',15000),
                (333,'Ashish Kumar Singh',66755555,25,'129, Real Housing, Goa',20000),
                (212,'Aman Bothra',444433,20,'420, Absolut Villas, Pune',22000),
                (245,'Zakee Ahmed',7654483,22,'554-C, Developed Residency, Jaipur',16000)]
    cur.executemany(data_sample,record1)

    pass_sample = ("insert into pass values(%s, %s)")
    record2 = [(111,'aaa'),
                (543,'bbb'),
                (333,'ccc'),
                (212,'ddd'),
                (245,'eee')]
    cur.executemany(pass_sample,record2)

    transaction_sample = ("insert into trans values(%s, %s, %s, %s, %s)")
    record3 = [(111,'2022-01-31 11:24:31', 'Deposit', 100, 'Account Created'),
                (543,'2022-01-31 11:25:53', 'Deposit', 100, 'Account Created'),
                (333,'2022-01-31 11:26:33', 'Deposit', 100, 'Account Created'),
                (212,'2022-01-31 11:27:45', 'Deposit', 100, 'Account Created'),
                (245,'2022-01-31 11:28:53', 'Deposit', 100, 'Account Created'),
                (111,'2022-01-31 11:29:42', 'Deposit', 9900, 'Sample deposit'),
                (543,'2022-01-31 11:30:53', 'Deposit', 14900, 'Sample deposit'),
                (333,'2022-01-31 11:31:12', 'Deposit', 19900, 'Sample deposit'),
                (212,'2022-01-31 11:32:55', 'Deposit', 21900, 'Sample deposit'),
                (245,'2022-01-31 11:33:06', 'Deposit', 15900, 'Sample deposit')]
    cur.executemany(transaction_sample,record3)
    mycon.commit()


