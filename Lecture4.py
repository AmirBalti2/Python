#condition statement 
#if statment 
name=input("Enter your name ")

if name=="Ali":
    print("Welcome Ali")
if name=="Amir":
    print("Welcome Amir")
if name=="":
    print("Empty")

if name!="Ali" and name!="Amir":
    print("Enter name Ali or Amir")

#guess number 

number=int(input("Enter the number "))
gussName=3
if number==gussName:
    print("You gussed the right number")
if number!=gussName:
    print("You gussed the wrong number")

#test the Math
option=input("choice the math  or Pakistan study Test")
if option=="math":
    print("You have selected Math\n 2+2 is enter the answer")
    answer=int(input())
    if answer==4:
        print("You have selected the right answer")
    if answer!=4:
        print("You have selected the wrong answer")
if option=="Pakistan study":
    print("You have selected Pakistan study\n Who is the founder of Pakistan")
    answer=input()
    if answer=="Quaid-e-Azam":
        print("You have selected the right answer")
    if answer!="Quaid-e-Azam":
        print("You have selected the wrong answer")
if option!="math" and option!="Pakistan study":
    print("You have selected the wrong option")
