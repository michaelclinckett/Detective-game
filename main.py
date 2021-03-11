import time
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")






print("You are a detective\n")
time.sleep(2)
print("Solve the case\n")
time.sleep(2)
print("Don't catch the wrong guy")
time.sleep(2)
input("Press enter to start")
time.sleep(2)
print("A murder was carried out on the 26th of October, 1976\n")
time.sleep(2)
print("4 suspects were caught and you are here to question them\n")
time.sleep(2)
print("ask questions")


