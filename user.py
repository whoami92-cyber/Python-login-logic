import time
import getpass
import os

attemps=0
while True:
    user=input("User: ")
    pw=getpass.getpass("Password: ")
    if  user =='admin' and pw =='1234':
        time.sleep(1)
        print("Hello")
        while True:
            key=input("Give list: ")
            a= ['A', 'AB', 'CD', 'EF']
            b= ['1','2','3', '4', '5']
            c=['PYTHON']
            if key==  'a':
                print (a)
            elif key == 'b':
                print (b)
            elif key =='c':
                print (c)
            if key =='exit':
                time.sleep(1)
                print ("bye")
                os.system('clear')
                break
    elif user == 'exit':
       break
    else:
       print("Error")
       attemps  +=1
       time.sleep(1)
       print ("attemps", attemps)
       time.sleep(2)
    if attemps == 3:
       print("wrong user or password")
       break
