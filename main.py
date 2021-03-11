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
print("Don't catch the wrong guy\n")
time.sleep(2)
input("Press enter to start level 1")
time.sleep(2)
print("\nA murder was carried out on the 26th of October, 1976\n")
time.sleep(2)
print("4 suspects were caught and you are here to question them\n")
time.sleep(2)
print("ask questions to find out who the murder is\n")
time.sleep(2)
print("Suspect 1 said he was at Kmart when the murder was commited\n")
time.sleep(2)
print("Suspect 2 said he saw a movie at the time of the murder\n")
time.sleep(2)
print("Suspect 3 said he was at home when victim was murdered\n")
time.sleep(2)
print("Suspect 4 said he was at home sleeping\n")
time.sleep(2)
print("\nThe murder was commited at 1 am in the morning\n")
try:
  murder=float(input("Who is the murder? (number of suspect)>>>"))
  if murder == 1:
    print("\nYou found the correct murder. ")
  else:
    print("\nYou got the wrong man. You are fired from your job and are fined $10000. Restart to try again")
except ValueError:
  quit("\nYou got fired for invalid input of suspect. Restart to try again")



