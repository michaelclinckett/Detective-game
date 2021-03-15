import time
from datetime import datetime
import os
# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")








  
time.sleep(2)
input("Press enter to start level 2")
time.sleep(2)
print("Use questions to find out who the thief is.")

while True:
  time.sleep(2)
  sentance=(input("\nAsk a question or put in a number of the suspect who commited the crime>>> "))
  if "where" and "you" in sentance:
    print("Suspect 1 was at a friends house")
    print("Suspect 2 was sleeping")
    print("Suspect 3 was eating dinner with his family")
    print("Suspect 4 was watching tv at home")
  if "time" in sentance:
    print("The theif struck at 9:00pm on Wednesday, 2009")
  if "alibi" in sentance:
    print("Suspect 1's friend says he was with him the whole time. They were at Pak'n'save till 10:00pm")
    print("Suspect 2's wife said that he went to bed at around 8:30pm")
    print("Suspect 3's family said he was eating pizza with them from 8:30 to 9:30 ")
    print("Suspect 4 does not have an alibi but aid he was watching Thomas the tank engine on TV")
  if "where" and "crime" in sentance:
    print("The crime was commited at the house next door to Pak'n'save")
  if "tv" in sentance:
    print("From 8pm to 9pm was Thomas the tank engine on TV")
  if "friend" and "what" in sentance:
    print("Suspect 1 and friend walked past the robbed house and went up the drive of the house according to a passbyer. He did not see them come out.")
  if sentance != "1" or "2" or "3" or "4":
    print("This question can not be answered")
  if sentance != "1":
    print("You are fired from your job. Restart to try again")
    quit()
  if sentance == "1":
    print("Great job, you got the man. He and his friend commited the crime togther.")
    break
print("entering level 3 (coming soon)")
   
