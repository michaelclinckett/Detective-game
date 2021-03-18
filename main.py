import time
from datetime import datetime
import os
# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")




print("You are a detective\n")
time.sleep(1)
print("Solve the case\n")
time.sleep(1)
print("Don't catch the wrong guy\n")
time.sleep(1)
input("Press enter to start level 1")
time.sleep(1)
print("\nA murder was carried out on the 26th of October, 1976\n")
time.sleep(1)
print("4 suspects were caught and you are here to find out who commited the murder\n")

time.sleep(1)
print("Suspect 1 said he was at Kmart at the time of the murder\n")
time.sleep(1)
print("Suspect 2 said he saw a movie at the time of the murder\n")
time.sleep(1)
print("Suspect 3 said he was at home when victim was murdered\n")
time.sleep(1)
print("Suspect 4 said he was at home sleeping\n")
time.sleep(1)
print("The murder was commited at 1 am in the morning\n")
try:
  murder=float(input("Who is the murder? (number of suspect)>>>"))
  if murder != 1:
    print("\nYou got the wrong man. You are fired from your job and are fined $10000. Restart to try again")
    quit()
  else:
    print("\nYou found the correct murderer. Reasons are Kmart is not open at 1am and Kmart did not exist in 1976.")
    time.sleep(1)
    print("Entering level 2")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')

except ValueError:
  quit("\nYou got fired for invalid input of suspect. Restart to try again")



  
time.sleep(1)
input("Press enter to start level 2")
time.sleep(1)
print("A computer, tv and ps5 were stolen. ")
time.sleep(1)
print("Find out who the thief is and ask the suspects and officers at the police station to find the thief by asking questions")


while True:
  time.sleep(1)
  sentence=(input("\nAsk a question or put in a number of the suspect who commited the crime\n>>> "))
  if "where" in sentence and "you" in sentence:
    print("Suspect 1 was at a friends house")
    print("Suspect 2 was sleeping")
    print("Suspect 3 was eating dinner with his family")
    print("Suspect 4 was watching tv at home")
  elif "time" in sentence:
    print("The theif struck at 9:00pm on Wednesday, 2009")
  elif "alibi" in sentence:
    print("Suspect 1's friend says he was with him the whole time. They were at Pak'n'save till 10:00pm")
    print("Suspect 2's wife said that he went to bed at around 8:30pm")
    print("Suspect 3's family said he was eating pizza with them from 8:30 to 9:30 ")
    print("Suspect 4 does not have an alibi but said he was watching Thomas the tank engine on TV")
  elif "where" in sentence and "crime" in sentence:
    print("The crime was commited at the house next door to Pak'n'save")
  elif "tv" in sentence:
    print("From 8pm to 9pm was Thomas the tank engine on TV")
  elif "friend" in sentence and "what" in sentence:
    print("Suspect 1 and friend walked past the robbed house and went up the drive of the house according to a passbyer. He did not see them come out.")
  elif sentence == "2" or sentence == "3" or sentence == "4":
    print("You are fired from your job. Restart to try again")
    quit()
  elif sentence == "1":
    print("Great job, you got the man. He and his friend commited the crime togther.")
    time.sleep(1)
    print("entering level 3")
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')
    break
  else: 
     print("This question can not be answered")
second_time=0
input("Press enter to start level 3")
print("A kidnapping has occured.")
time.sleep(1)
print("There are 4 suspects and each one has a personality")
time.sleep(1)
print("Ask questions to find the kidnapper. Remember, each suspect has a personality so the suspects may not answer your questions straight away and truthfully")
while True:
  time.sleep(1)
  sentence=(input("\nAsk a question or put in a number of the suspect who commited kidnapping\n>>> "))
  if "where" in sentence and "you" in sentence:
    print("Suspect 1 refuses to answer")
    print("Suspect 2 was at work")
    print("Suspect 3 was was peforming at a show")
    print("Suspect 4 was watching suspect 3 on tv")
  elif "time" in sentence:
    print("The kidnapping happened at 6:00pm on Thursday, 18th of March, 2021")
  elif "alibi" in sentence and second_time == 0:
    second_time == 1
    print("Suspect 1 refuses to answer")
    print("Suspect 2 co-worker says he was at work till 8:00pm")
    print("Suspect 3 had over 1000 alibis ")
    print("Suspect 4 does not have an alibi but says he was watching suspect 3 on tv till the show ended")
  elif "where" in sentence and "crime" in sentence:
    print("The kidnapping happened at house number 5 on third avenue")
  elif "tv" in sentence or "show" in sentence or "performence" in sentence:
    print("From 6pm to 9pm suspect 3 performed his 1 man women interpretation. This was broadcasted on tv")
  elif "alibi" in sentence and second_time == 1:
    print("Suspect 1 said he has no alibi")
    print("Suspect 2 co-worker says he was at work till 8:00pm")
    print("A fan at the show got a signature of suspect 3.")
    print("Suspect 4 does not have an alibi but says he was watching suspect 3 on tv till the show ended")
    second_time == 0
  elif "signature" in sentence:
    print("suspect 1 says he doesn't have a signature")
    print("Suspect 2 has a signature but can be confirmed that that is his signature")
    print("Suspect 3's signature does not match the one taken at the show")
    print("Suspect 4's signature can not be confirmed")
  elif sentence == "2" or sentence == "1" or sentence == "4":
    print("You are fired from your job. Restart to try again")
    quit()
  elif sentence == "3":
    print("Great job, you got the man. He switched places with his twin sister at the show and commited the kidnapping.")
    break
  else: 
     print("This question can not be answered")
print("CONGRATS!!! You finished the detective game. You are now a qualified detective")









