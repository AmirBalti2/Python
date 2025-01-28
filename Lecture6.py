#string Methode 
#captilized method 
user_name="ali Is Ali pakistan and 676 Age"
print("Capilitzed method is {}".format(user_name.capitalize()))
#caseflod method
string1 = "Straße"
string2 = "STRASSE"

print(string1.lower() == string2.lower())    # Output: False
print(string1.casefold() == string2.casefold())  # Output: True

print(string1.center(100, '1'))  # Output: *******Straße*******

#Mini Projects find word in string
Word = input("Enter a word: ")
find= input("Enter a letter to find: ")
print("The letter is found {} times in the word".format(Word.count(find)))
#Mini Projects find word in string and replace it with another word

Word = input("Enter a word: ")
find= input("Enter a letter to find: ")
replace= input("Enter a letter to replace: ")
print("The letter is found {} times in the word".format(Word.replace(find,replace)))
#Project: Username Generator
import random
random_num=random.randint(0,10)
frist_name=input("Enter your name: ")
last_name=input("Enter your last name: ")
frist_name=frist_name.capitalize()
last_name=last_name.capitalize()
frist_name=frist_name.strip()
last_name=last_name.strip()
frist_name=frist_name.lower()
last_name=last_name.lower()
user_name=frist_name+last_name+str(random_num)

print("Your username is:{}".format(user_name))