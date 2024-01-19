#This File is the main user interface of this program ie. main menu 

import time
def ldash(n = 40):
    print('-'*n)
def leq(n = 40):
    print('='*n)

def menu():
    time.sleep(0.1)
    global num
    leq()
    print("\t\tXYZ Bank")
    leq()
    time.sleep(0.1)
    print("Enter (1) to Create new account")
    time.sleep(0.1)
    print("Enter (2) to Login")
    time.sleep(0.1)
    print("Enter (exit) to Exit the program")
    leq()
    time.sleep(0.5)
    num = str(input("Enter choice: "))
    time.sleep(0.1)
