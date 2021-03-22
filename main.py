import time
from datetime import datetime
import os
from random import*   
# datetime object containing current date and time
now = datetime.now()
 

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


Suspect_number_choice=['1','2','3','4']                           
selector=choice(Suspect_number_choice)    

if selector == '1':
  suspect_1='1'
  suspect_2='2'
  suspect_3='3'
  suspect_4='4'
elif selector == '2':
  suspect_1='4'
  suspect_2='1'
  suspect_3='2'
  suspect_4='3'
elif selector == '3':
  suspect_1='3'
  suspect_2='4'
  suspect_3='1'
  suspect_4='2'
elif selector == '4':
  suspect_1='2'
  suspect_2='3'
  suspect_3='4'
  suspect_4='1'

def start_up():
  print("You are a detective\n")
  time.sleep(1)
  print("Solve the case\n")
  time.sleep(1)
  print("Don't catch the wrong guy\n")
  time.sleep(1)
  customerNum = input("Press enter to start level 1")
  if customerNum == '1':
    level1()
  elif customerNum == '2':
    level2()
  elif customerNum == '3':
    level3()
  time.sleep(1)
def level1():
    
  print("\nA murder was carried out on the 26th of October, 1976\n")
  time.sleep(1)
  print("4 suspects were caught and you are here to find out who commited the murder\n")

  time.sleep(1)
  print("Suspect", suspect_1, "said he was at Kmart at the time of the murder\n")
  time.sleep(1)
  print("Suspect", suspect_2, "said he saw a movie at the time of the murder\n")
  time.sleep(1)
  print("Suspect", suspect_3, "said he was at home when victim was murdered\n")
  time.sleep(1)
  print("Suspect", suspect_4, " said he was at home sleeping\n")
  time.sleep(1)
  print("The murder was commited at 1 am in the morning\n")
  try:
    murder=float(input("Who is the murder? (number of suspect)>>>"))
    if murder != suspect_1:
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



def level2():  
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
      print("Suspect", suspect_1, "was at a friends house")
      print("Suspect", suspect_2, " was sleeping")
      print("Suspect", suspect_3, " was eating dinner with his family")
      print("Suspect", suspect_4, " was watching tv at home")
    elif "time" in sentence:
      print("The thief struck at 9:00pm on Wednesday, 2009")
    elif "alibi" in sentence:
      print("Suspect", suspect_1, "'s friend says he was with him the whole time. They were at Pak'n'save till 10:00pm")
      print("Suspect", suspect_2, "'s wife said that he went to bed at around 8:30pm")
      print("Suspect", suspect_3, "'s family said he was eating pizza with them from 8:30 to 9:30 ")
      print("Suspect", suspect_4, " does not have an alibi but said he was watching Thomas the tank engine on TV")
    elif "where" in sentence and "crime" in sentence:
      print("The crime was commited at the house next door to Pak'n'save")
    elif "tv" in sentence:
      print("From 8pm to 9pm was Thomas the tank engine on TV")
    elif "friend" in sentence and "what" in sentence:
      print("Suspect", suspect_1, " and friend walked past the robbed house and went up the drive of the house according to a passbyer. He did not see them come out.")
    elif sentence == suspect_2 or sentence == suspect_3 or sentence == suspect_4:
      print("You are fired from your job. Restart to try again")
      quit()
    elif sentence == suspect_1:
      print("Great job, you got the man. He and his friend commited the crime togther.")
      time.sleep(1)
      print("entering level 3")
      time.sleep(4)
      os.system('cls' if os.name == 'nt' else 'clear')
      break
    else: 
      print("This question can not be answered")
def level3():
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
      print("Suspect", suspect_1, "refuses to answer")
      print("Suspect", suspect_2, "was at work")
      print("Suspect", suspect_3, " was was peforming at a show")
      print("Suspect", suspect_4, " was watching suspect 3 on tv")
    elif "time" in sentence:
      print("The kidnapping happened at 6:00pm on Thursday, 18th of March, 2021")
    elif "alibi" in sentence and second_time == 0:
      second_time == 1
      print("Suspect", suspect_1, " refuses to answer")
      print("Suspect", suspect_2, " co-worker says he was at work till 8:00pm")
      print("Suspect", suspect_3, " had over 1000 alibis ")
      print("Suspect", suspect_4, " does not have an alibi but says he was watching suspect 3 on tv till the show ended")
    elif "where" in sentence and "crime" in sentence:
      print("The kidnapping happened at house number 5 on third avenue")
    elif "tv" in sentence or "show" in sentence or "performence" in sentence:
      print("From 6pm to 9pm suspect 3 performed his 1 man women interpretation. This was broadcasted on tv")
    elif "alibi" in sentence and second_time == 1:
      print("Suspect", suspect_1, " said he has no alibi")
      print("Suspect", suspect_2, " co-worker says he was at work till 8:00pm")
      print("A fan at the show got a signature of suspect ", suspect_3, )
      print("Suspect", suspect_4, " does not have an alibi but says he was watching suspect 3 on tv till the show ended")
      second_time == 0
    elif "signature" in sentence:
      print("suspect", suspect_1, " says he doesn't have a signature")
      print("Suspect", suspect_2, " has a signature but can be confirmed that that is his signature")
      print("Suspect", suspect_3, "'s signature does not match the one taken at the show")
      print("Suspect", suspect_4, "'s signature can not be confirmed")
    elif sentence == suspect_1 or sentence == suspect_2 or sentence == suspect_4:
      print("You are fired from your job. Restart to try again")
      quit()
    elif sentence == suspect_3:
      print("Great job, you got the man. He switched places with his twin sister at the show and commited the kidnapping.")
      break
    else: 
      print("This question can not be answered")
def ending():
  print("CONGRATS!!! You finished the detective game. You are now a qualified detective")



start_up()
level1()
level2()
level3()
ending()




