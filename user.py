import time
import getpass

attemps=0
while True:
    user=input("User: ")
    pw=getpass.getpass("Password: ")
    if  user =='admin' and pw =='1234':
        time.sleep(1)
        print("Hello")
        a= ['A', 'AB', 'CD', 'EF']
        print (a)
        time.sleep(1)
        print("bye")
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
