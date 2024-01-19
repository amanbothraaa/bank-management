#This file handles user login in this program

from asyncio import sleep
from colorama import Fore,Style
import mainmenu as m1
import random
import mysql.connector as sqltor
import config
import pwinput as pp
import time

#establishing the connection to mysql server
mycon = sqltor.connect(
    host = 'localhost',
    user = config.mysql_user,
    passwd = config.mysql_passwd,
    database = 'bank'
)
#Checking if python program is able to make connection to mysql server 
if mycon.is_connected() == False:
   print('Could not connect to database...')

#Creating a sql cursor   
cur = mycon.cursor()

#Program that runs when the user wants to login and access further.
def acc_login():
    cur.execute("select AccNo from data")
    acc_data = cur.fetchall()
    allacc_no = []
    for a in acc_data:
        allacc_no.append(a[0])
    #print(allacc_no)
    ch = ''
    while ch.lower() != "x":
        if ch.lower() != "x":
            m1.ldash()
            print("|\t\t Login\t\t       |")
            m1.ldash()
            accno = int(input("Enter account number: "))
        if accno in allacc_no:
            while ch.lower() != 'z':
                if ch.lower() == "x":
                    break
                pass_input = str(pp.pwinput(prompt="Enter password: ", mask="*"))
                cur.execute("select Password from pass where AccNo = {}".format(accno))
                pass_true = cur.fetchone()
                cur.execute("select * from data where AccNo = {}".format(accno))
                alldata = cur.fetchall()    
                if pass_input == pass_true[0]:
                    while ch.lower() != 'x' or ch.lower() != 'z':
                        fields = ['Account Number','Name','Phone','Age','Address','Balance']
                        print('\n')
                        m1.leq()
                        print("Welcome",(alldata[0][1]).title(),"!")
                        m1.leq()
                        time.sleep(0.1)
                        print("Press (1) to View User Details")
                        time.sleep(0.1)
                        print("Press (2) to Deposit money")
                        time.sleep(0.1)
                        print("Press (3) to Withdraw money")
                        time.sleep(0.1)
                        print("Press (4) to View Transaction Log")
                        time.sleep(0.1)
                        print('Press (X) to Return to Main Menu')
                        time.sleep(0.1)
                        m1.ldash()
                        ch = input("Enter 1/2/3/4/X: ")
                        m1.ldash()
                        time.sleep(0.2)

                        if ch == '1':
                            for a in range(6):
                                print(fields[a],':',alldata[0][a]) 
                                m1.ldash()
                                time.sleep(0.1)
                            time.sleep(3) 
                        if ch == '2':
                            dep = float(input("Enter amount to deposit: ")) 
                            time.sleep(0.1)
                            rem = str(input("Remark: "))
                            if rem == '':
                                rem = '-'
                            cur.execute("update data set balance = balance+{} where accno = {};".format(dep,accno))
                            cur.execute("insert into trans values({},now(),'{}',{},'{}');".format(accno,'Deposit',dep,rem))
                            mycon.commit()
                            time.sleep(0.1)
                            print('.')
                            time.sleep(0.2)
                            print('..')
                            time.sleep(0.2)
                            print('...')
                            time.sleep(0.2)
                            
                            print('Rs',dep,'added to your account successfully!')
                            cur.execute("select * from data where AccNo = {}".format(accno))
                            alldata = cur.fetchall()    
                            #Updating the deposit for the temp python list 'alldata'
                            time.sleep(3)

                        if ch == '3':
                            wit = float(input("Enter amount to withdraw: "))
                            time.sleep(0.1)
                            if wit <= alldata[0][5]-100:
                                rem = str(input("Remark: "))
                                time.sleep(0.2)
                                if rem == '':
                                    rem = '-'
                                cur.execute("insert into trans values({},now(),'{}',{},'{}');".format(accno,'Withdrawal',dep,rem))
                                cur.execute("update data set balance = balance-{} where accno = {};".format(wit,accno))
                                mycon.commit()
                                m1.ldash()
                                print('Rs',wit,'withdrawn from your account! ')
                                print('.')
                                time.sleep(0.2)
                                print('..')
                                time.sleep(0.2)
                                print('...')
                                time.sleep(0.2)                                                                                               
                                print('Please collect the cash!')
                                m1.ldash()
                                time.sleep(3)
                                cur.execute("select * from data where AccNo = {}".format(accno))
                                alldata = cur.fetchall()    
                                #Updating the deposit for the temp python list 'alldata'

                            else:
                                print('Your account has a balance of',alldata[0][5])
                                time.sleep(0.1)
                                print('You can\'t withdraw more than what you have!')
                                time.sleep(0.1)
                                print('The minimum balance in your bank account can\'t go below 100.')

                        if ch == '4':
                            cur.execute("select * from trans where AccNo = {}".format(accno))
                            transaction_data = cur.fetchall() 
                            fields2 = ['Date/Time','Transaction','Amount','Remarks']
                            m1.ldash(70)
                            print('   {:15s}     {:10s}\t {:6s}\t         {:30s}'.format(fields2[0],fields2[1],fields2[2],fields2[3]))
                            m1.ldash(70)
                            time.sleep(0.1)
                            for b in transaction_data:
                                if b[2] == "Deposit":
                                    print(Fore.GREEN,'{}\t{:10s}\t{:7.2f}\t\t{:30s}'.format(b[1],b[2],b[3],b[4]),Style.RESET_ALL)
                                    time.sleep(0.3)
                                if b[2] == "Withdrawal":
                                    print(Fore.RED,'{}\t{:10s}\t{:7.2f}\t\t{:30s}'.format(b[1],b[2],b[3],b[4]),Style.RESET_ALL)
                                    time.sleep(0.3)
                            m1.ldash(70)
                            time.sleep(3)
                        if ch.lower() == 'x':
                            break
                    
                else:
                    print()
                    print("Wrong password!")
                    m1.ldash()
                    time.sleep(0.1)
                    print('PRESS x to return to main menu')
                    time.sleep(0.1)
                    print('PRESS z to return to Login again')
                    time.sleep(0.1)
                    m1.ldash()
                    time.sleep(0.15)
                    ch = input("Enter here(x/z): ")
                    if ch.lower() == 'x':
                        print()
                        break
            if ch.lower() == 'x':
                break
            else:
                ch = ''
        else:
            m1.ldash()
            print("Account number",accno,"does not exist!")
            m1.ldash()
            print('PRESS x to return to main menu')
            print('PRESS z to return to Login again')
            m1.ldash()
            ch = input("Enter here(x/z): ")
            if ch.lower() == 'x':
                print()
            else:
                ch = ''
    ch = ''    
