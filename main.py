n = input("Hello, what is your name? ")

x = input(
  f'Kia Ora {n} Would you like to play a maori language quiz? ').lower()




if x == "yes" or x == "y":
 q1 = input("What is the maori word for Coding? ").lower()
if q1 == "whakawaehere":
 print("Correct!")
else:
  exit("Incorrect")
  
q2 = input("What is the maori word for Hard Drive? ").lower()
if q2 == "pumaro":
  print("Correct!")
else:
  exit("Incorrect")
  
q3 = input("What is the maori word for input?  ").lower()
if q3 == "tauru":
 print("Correct!")
else:
  exit("Incorrect")
  
q4 = input("What is the maori word for output? ").lower()
if q4 == "pungao puta":
   print("Correct")
else:
  exit("Incorrect")
  
q5 = input("what is the maori word for programming? ").lower()
if q5 == "putirotiro":
  print("Correct")
else:
  exit("Incorrect")