#Author Amir Hussain
#Date: 10/10/2019
#Project Game Assistant Bot

#get user Prompt 
display="Welcome to the chatbot"
print(display.center(100,"*"))


while True:
    user_prompt=input("Ask me a game tip: ").lower()
    if user_prompt in ["hey","hello","hi"]:
        print("Hello I am a game assistant bot")
    elif user_prompt in ["gta cheat","minecraft","pubg","call of duty","fortnite"]:
        if(user_prompt=="gta cheat"):
            message="""what cheat you want to know\n 1. Health cheat\n 
            2. Money cheat\n 3. Weapons cheat\n 4. Vehicle cheat\n"""
            print(message.center(100,"*"))
            sub_choice=input("Enter the cheat number: ")
            if sub_choice=="1":
                print("Health cheat is: HESOYAM")
                break
            elif sub_choice=="2":
                print("Money cheat is: ROCKETMAN")
                break
            elif sub_choice=="3":
                print("Weapons cheat is: UZUMYMW")
                break
            elif sub_choice=="4":
                print("Vehicle cheat is: AIWPRTON")
                break
            else:
                print("Invalid choice")
        elif(user_prompt=="minecraft"):
            message="""what cheat you want to know\n 1. Health cheat\n 
            2. Money cheat\n 3. Weapons cheat\n 4. Vehicle cheat\n"""
            print(message.center(100,"*"))
            sub_choice=input("Enter the cheat number: ")
            if sub_choice=="1":
                print("Health cheat is: HESOYAM")
                break
            elif sub_choice=="2":
                print("Money cheat is: ROCKETMAN")
                break
            elif sub_choice=="3":
                print("Weapons cheat is: UZUMYMW")
                break
            elif sub_choice=="4":
                print("Vehicle cheat is: AIWPRTON")
                break
            else:
                print("Invalid choice")
        elif(user_prompt=="pubg"):
            message="""what cheat you want to know \n 1. Health cheat\n 
            2. Money cheat\n 3. Weapons cheat\n 4. Vehicle cheat\n"""
            print(message.center(100,"*"))
            sub_choice=input("Enter the cheat number: ")
            if sub_choice=="1":
                print("Health cheat is: HESOYAM")
                break
            elif sub_choice=="2":
                print("Money cheat is: ROCKETMAN")
                break
            elif sub_choice=="3":
                print("Weapons cheat is: UZUMYMW")
                break
            elif sub_choice=="4":
                print("Vehicle cheat is: AIWPRTON")
                break
            else:
                print("Invalid choice")
    elif user_prompt in ["Exit","Quit"]:
        print("Goodbye! Have a nice day")
        break
    else:
        print("I am sorry I am not able to understand you")
        break
# End of the program


