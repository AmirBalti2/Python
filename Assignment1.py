#Task 1 Prints a message like: City A is hotter than City B.
tem_cityA=float(input("Enter the temperature of city A "))
tem_cityB=float(input("Enter the temperature of city B "))

print(f"City A is hotter than City B: {tem_cityA > tem_cityB}")
print(f"City A is colder than City B: {tem_cityA < tem_cityB}")
print(f"City A and City B have the same temperature: {tem_cityA == tem_cityB}")
print(f"City A and City B have different temperatures: {tem_cityA != tem_cityB}")

#Part 2: Bill Splitter

totalAmount=int(input("Enter the total amount "))
totalPeople=int(input("Enter the total number of peoples "))
print(
    "Total Bill: ${0} \n Number of Peoples: {1} \n Share: ${2} ".format(totalAmount,totalPeople,
                                                                       (totalAmount/totalPeople))
    ) 


print("{} Loves the Color {} and their favorite number is ".format(input("Enter ur Name"),input("Enter ur favorite color"),
                                                                   input("Enter ur favorite number"),)
      ) 


#Task 5

length=float(input("Enter the length of the rectangular "))
width=float(input("Enter the width of the rectangular "))

print("Length: {} \n Width: {} \n area: {} \n Perimeter {}".format(length,width,
(length*width),(2*(length+width))))
#task 6 Age Difference Calculator

age_p1=float(input("Enter the age of frist person "))
age_p2=float(input("Enter the the age of second person "))

print("The age difference between: person1 and peron2 is {} ".format((abs(age_p1-age_p2))))
#Task 7
days=int(input("Enter the number of days "))
print("{} days are equal to {} seconds. ".format(days,(days*24*60*60)))

#task 8
Number1=int(input("Enter frist number "))
Number2=int(input("Enter second number "))
operator=input("Enter operator (+, -, *, /)")

result_ = (operator == "+") * "{} + {} = {}".format(Number1, Number2, (Number1 + Number2)) + \
         (operator == "-") * "{} - {} = {}".format(Number1, Number2, (Number1 - Number2)) + \
         (operator == "*") * "{} * {} = {}".format(Number1, Number2, (Number1 * Number2)) + \
         (operator == "/" and Number2 != 0) * "{} / {} = {}".format(Number1, Number2, (Number1 / Number2)) + \
         (operator == "/" and Number2 == 0) * "Division by zero is undefined." + \
         (operator not in "+-*/") * "Invalid operator."

# Print the result
print(result_)

#task4
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

result = (num_1 > num_2) * f"{num_1} is greater than {num_2}" + \
         (num_1 < num_2) * f"{num_1} is less than {num_2}" + \
         (num_1 ==num_2) * f"{num_1} is equal to {num_2}"
print(result)

even=(num_1%2==0)*(num_2%2==0)*" both are event"+\
      (num_1%2==1)*(num_2%2==1)*" both are odd"+\
      (num_1%2==0)*(num_2%2==1)*" One number is even and the other is odd."+\
      (num_1%2==1)*(num_2%2==0)*" One number is odd and the other is even."
print(even)
