import time
from datetime import datetime
import os
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

while True:
  time.sleep(2)
  sentance=(input("\nAsk a question or put in a number of the suspect who commited the crime>>>"))
  if "where" and "you" in sentance:
    print("Suspect 1 was at a friends house")
    print("Suspect 2 was sleeping")
    print("Suspect 3 was eating dinner with his family")
    print("Suspect 4 was watching tv at home")
  elif "time" in sentance:
    print("The theif struck at 9:00pm on Wednesday, 2009")
  elif "alibi" in sentance:
    print("Suspect 1's friend says he was with him the whole time")
    print("Suspect 2's wife said that he went to bed at around 8:30pm")
    print("Suspect 3's family said he was eating dinner from 8:30 to 9:30 ")
    print("Suspect 4 does not have an alibi")
  elif "where" and "crime" in sentance:
    print("The crime was commited at the house next door to Pak'n'save")
  elif "what" and "doing" and "were" in sentance:
    print("Suspect 1 was at Pak'n'save with his friend")
    print("Suspect 2 was sleeping")
    print("Suspect 3 was eating pizza t home with his family")
    print("Suspect 4 was at home watching Thomas the tank engine on tv")
  elif "tv" in sentance:
    print("From 8pm to 9pm was Thomas the tank engine on TV")
  elif "friend" and "what" in sentance:
    print("Suspect 1 and friend walked past the robbed house and went up the drive of the house according to a passbyer. He did not see them come out.")
  
  elif "2" or "3" or "4" in sentance:
    print("You are fired from your job. Restart to try again")
    quit()
  elif "1" or "suspect 1" in sentance:
    print("Great job, you got the man. He and his friend commited the crime togther.")
    break
  else: 
    print("This qusetion cannot be answered")
print("entering level 3 (coming soon)")
   
