# Magic 8 ball 

name = "James"
question = "Will it rain this evening?"
answer = ""

import random
random_number = random.randint(1,11)
#print(random_number)

if question == "":
  print("Magic 8-Ball cannot provide a fourtune unless you ask it something.")
if name == "":
  print("question: " + question)
if random_number == 1:
  print("Yes- definitley.")
 
elif random_number == 2:
   print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")   
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")   
elif random_number == 8:
  print("Outlook not so good.")  
elif random_number == 9:
  print("Very doubtful.")  
elif random_number == 10:
  print("nah, bruh.")  
elif random_number == 11:
  print("Yes, 100X YES!")   
else:
  answer = "Error"  
  
print(name + " ask: " + question) 
print("Magic 8-Ball's answer: " + answer)  
