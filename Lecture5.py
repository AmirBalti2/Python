#if else if and nested if else statement

print("""--------welcome to the News World
      best news agency --------""")
choice=input("choice the news \n 1. World news\n 2. Local News\n 3. sport news\n 4. business news\n")

if choice=="1":
    print("You have selected the World news")
    sub_choice=input("choice the news \n 1. Pelatinse and israel \n 2. Mr Trump fuck his dog\n 3. Russia warning US \n 4. Alien reach in Trump ceremory\n")
    if(sub_choice=="1"):
        print("""Today Hamas and israel reach on deal and relaease 
              their peoples. Today morning is a sign of relif for 
              the people of Gaza after one year of gencoide and hungry 
              people came out for basic aids. The world close eye on the 
              gaza and gave SSS isreali army free hand to kill and 
              rape people in gaza say Al Hamaz bin waleed. read more about click here wwww.fin.com""")
    elif(sub_choice=="2"):
          print("""Today Hamas and israel reach on deal and relaease 
              their peoples. Today morning is a sign of relif for 
              the people of Gaza after one year of gencoide and hungry 
              people came out for basic aids. The world close eye on the 
              gaza and gave SSS isreali army free hand to kill and 
              rape people in gaza say Al Hamaz bin waleed. read more about click here wwww.fin.com""")
    elif(sub_choice=="3"):

     print("""Today Hamas and israel reach on deal and relaease 
              their peoples. Today morning is a sign of relif for 
              the people of Gaza after one year of gencoide and hungry 
              people came out for basic aids. The world close eye on the 
              gaza and gave SSS isreali army free hand to kill and 
              rape people in gaza say Al Hamaz bin waleed. read more about click here wwww.fin.com""")
    elif(sub_choice=="4"):
          print("""Today Hamas and israel reach on deal and relaease 
              their peoples. Today morning is a sign of relif for 
              the people of Gaza after one year of gencoide and hungry 
              people came out for basic aids. The world close eye on the 
              gaza and gave SSS isreali army free hand to kill and 
              rape people in gaza say Al Hamaz bin waleed. read more about click here wwww.fin.com""")
    else:
        print("Invalid choice")
elif choice=="2":
    print("You have selected the Local news")
    sub_choice=input("choice the news \n 1. Pakistan face the water crisis\n 2. PPPP has a history of corruption\n 3. PTI has a history of corruption\n 4. PMLN has a history of corruption\n")
    if(sub_choice=="1"):
        print("""pakistani people are facing the water crisis and drinking water is not aviable for the 
              people of pakistan. The government of pakistan is not taking any action on this issue and solve it 
              as soon as possible. The people of pakistan are facing the water crisis and the government is not taking any action on this issue. read more about click here wwww.fin.com""")
    elif(sub_choice=="2"):
        print("""PPPP is consider the most corrupt party in the history of pakistan and 
              they have a history of corruption. The people of pakistan are not happy with the performance of PPPP and they are not happy with the performance of PPPP. The people of pakistan are not happy with the performance of PPPP 
              and they are not happy with the performance of PPPP. read more about click here wwww.fin.com""")
    else:
        print("Invalid choice")
elif choice=="3":
    print("You have selected the sport news")
    sub_choice=input("choice the news \n 1. Pakistan win the cricket match\n 2. Pakistan lose the cricket match\n 3. Pakistan win the hockey match\n 4. Pakistan lose the hockey match\n")
    if(sub_choice=="1"):
        print("""Pakistan win the cricket match against india and the people of pakistan are very happy with the performance of the pakistan cricket team. The people of pakistan are very happy with the performance of the pakistan cricket team and they are very happy with the performance of the pakistan cricket team. read more about click here wwww.fin.com""")
    elif(sub_choice=="2"):
        print("""Pakistan lose the cricket match against india and the people of pakistan are not happy with the performance of the pakistan cricket team. The people of pakistan are not happy with the performance of the pakistan cricket team and they are not happy with the performance of the pakistan cricket team. read more about click here wwww.fin.com""")
    else:
        print("Invalid choice")
elif choice=="4":
    print("You have selected the business news")
    sub_choice=input("choice the news \n 1. Pakistan stock exchange\n 2. Pakistan currency exchange\n 3. Pakistan business news\n 4. Pakistan trade news\n")
    if(sub_choice=="1"):
        print("""Pakistan stock exchange is going down and the people of pakistan are not happy with the performance of the pakistan stock exchange. The people of pakistan are not happy with the performance of the pakistan stock exchange and they are not happy with the performance of the pakistan stock exchange. read more about click here wwww.fin.com""")
    elif(sub_choice=="2"):
        print("""Pakistan currency exchange is going down and the people of pakistan are not happy with the performance of the pakistan currency exchange. The people of pakistan are not happy with the performance of the pakistan currency exchange and they are not happy with the performance of the pakistan currency exchange. read more about click here wwww.fin.com""")
    else:
        print("Invalid choice")
else:
    print("Invalid choice")
#string indexing 
user_name="Ali"
print(user_name[::1])