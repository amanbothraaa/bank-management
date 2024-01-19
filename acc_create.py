#This file handles Account creation of the user


import mainmenu as m1
import random
import mysql.connector as sqltor
import config
import pwinput as pp



#establishing the connection
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




cur.execute("select AccNo from data")
acc_data = cur.fetchall()
allacc_no = []
for a in acc_data:
    allacc_no.append(a[0])
#print(allacc_no)

def acc_create():
    m1.ldash()
    print("|\t   Create New Account  \t       |")
    m1.ldash()
    name = str(input("Enter Name: "))
    def input_ph(phone_no):
        while True:
            try:
                user_ph = int(input(phone_no))
            except ValueError:
                print("Invalid Number! Please insert a valid phone number.")
            else:
                return user_ph
                
    phone = input_ph("Enter Phone: ")
    

    def input_age(age_no):
        while True:
            try:
                user_age = int(input(age_no))
            except ValueError:
                print("Invalid Age! Please insert a valid age.")
            else:
                return user_age
                
    age = input_age("Enter Age: ")
    address = str(input("Enter Address: "))
    accno = random.randint(100,999)
    while accno in allacc_no: #Ensuring the accno remains unique
        accno = random.randint(100,999)
    if accno not in allacc_no:
        cur.execute("insert into data values({},'{}',{},{},'{}',{})".format(accno,name.title(),phone,age,address,100))
    mycon.commit()

    password1 = str(pp.pwinput(prompt="Create new password: ", mask="*"))
    password2 = str(pp.pwinput(prompt="Re-enter New Password:", mask="*"))
    if password1 != password2:
        while password1 != password2:
            print("Passwords do not match!")
            password1 = str(pp.pwinput(prompt="Create new password: ", mask="*"))
            password2 = str(pp.pwinput(prompt="Re-enter New Password: ", mask="*"))
    m1.ldash()
    print("Account Created Successfully!")
    print("You will be able to manage funds after logging in.")
    m1.leq()
    print("Your Account Number:",accno)
    print("Remember this detail!")
    m1.leq()
    print('\n')
    cur.execute("insert into pass values({},'{}')".format(accno,password1))
    mycon.commit()
    cur.execute("insert into trans values({},now(),'Deposit',100,'Account Created')".format(accno))
    mycon.commit()
