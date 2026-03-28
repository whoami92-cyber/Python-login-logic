import time
import getpass
attempst=0
while True:
    user=input("User: ")
    pw=getpass.getpass("Password: ")
    if user =='admin' and pw =='1234':
        print("Hello")
        break
    else:
       print("Error")
       attempst  +=1
       time.sleep(2)
    if attempst == 3:
       print("wrong user or password")
       break
