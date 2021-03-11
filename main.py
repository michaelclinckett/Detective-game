import time
from datetime import datetime
import os
# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


str = "Messi is the best soccer player"
>>> "soccer" in str
True
>>> "football" in str
False



print("You are a detective\n")
time.sleep(2)
print("Solve the case\n")
time.sleep(2)
print("Don't catch the wrong guy\n")
time.sleep(2)
input("Press enter to start level 1")
time.sleep(2)
print("\nA murder was carried out on the 26th of October, 1976\n")
time.sleep(2)
print("4 suspects were caught and you are here to find out who commited the murder\n")

time.sleep(2)
print("Suspect 1 said he was at Kmart at the time of the murder\n")
time.sleep(2)
print("Suspect 2 said he saw a movie at the time of the murder\n")
time.sleep(2)
print("Suspect 3 said he was at home when victim was murdered\n")
time.sleep(2)
print("Suspect 4 said he was at home sleeping\n")
time.sleep(2)
print("The murder was commited at 1 am in the morning\n")
try:
  murder=float(input("Who is the murder? (number of suspect)>>>"))
  if murder != 1:
    print("\nYou got the wrong man. You are fired from your job and are fined $10000. Restart to try again")
    quit()
  else:
    print("\nYou found the correct murderer. Reasons are Kmart is not open at 1am and Kmart did not exist in 1976.")
    time.sleep(2)
    print("Entering level 2")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')

except ValueError:
  quit("\nYou got fired for invalid input of suspect. Restart to try again")

time.sleep(2)
input("Press enter to start level 2")
time.sleep(2)
print("Use questions to find out who the thief is.")

