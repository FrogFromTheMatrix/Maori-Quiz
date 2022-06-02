counter = 3

n = input("Hello, what is your name? ")

x = input(
  f'Kia Ora {n} Would you like to play a maori language quiz? ').lower()



if x == "yes" or x == "y":
 print("You have 3 lives!")
   
 q1 = input("What is the maori word for Coding? ").lower()
 if q1 == "whakawaehere":
      print(f'Correct! you have still have {counter} lives left!' )
 else:
    counter -= 1
    print(f'Incorrect, You now have {counter} lives left!')
    
  
     
 q2 = input("What is the maori word for Hard Drive? ").lower()
 if q2 == "pumaro":
      print(f'Correct! you have still have {counter} lives left!' )
 else:
   counter -= 1
   print(f'Incorrect, You now have {counter} lives left!')
    
  
    
 q3 = input("What is the maori word for input?  ").lower()
 if q3 == "tauru":
     print(f'Correct! you have still have {counter} lives left!' )
 else:
    counter -= 1
    print(f'Incorrect, You now have {counter} lives left!')
      
  
    
 q4 = input("What is the maori word for output? ").lower()
 if q4 == "pungao puta":
       print(f'Correct! you have still have {counter} lives left!' )
 else:
      counter -= 1
      print(f'Incorrect, You now have {counter} lives left!')
    
  
    
 q5 = input("what is the maori word for programming? ").lower()
 if q5 == "putirotiro":
      print(f'Correct! you have still have {counter} lives left!' )
 else:
      counter -= 1
      print(f'Incorrect, You now have {counter} lives left!')
      
  
      
 q6 = input("what is the maori word for print? ").lower()
 if q6 == "matatuhi":
      print(f'Correct! you have still have {counter} lives left!' )
 else:
      counter -= 1
      print(f'Incorrect, You now have {counter} lives left!')
      
  
  
 q7 = input("what is the maori word for print? ").lower()
 if q7 == "matatuhi":
      print(f'Correct! you have still have {counter} lives left!' )
 else:
      counter -= 1
      print(f'Incorrect, You now have {counter} lives left!')
      
else:
 print("GoodBye")