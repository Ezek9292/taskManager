# write a program to calculate the average of 2 numbers

# take 2 numbers as input

nam1 = float(input("input a number"))
nam2 = float(input("input another number"))
# declare the average variable
# declare average =(num1 + num2)/2
# display the average
average = float(nam1 + nam2)/2
# print(f"Your avergae is: {average}")

# accept an age input from the user and a full name
# if the age is less than 18 and the average is equal to 20, print {name}, you are not allowed to vote
# if the age is greater than or equal to 18 and the average is greater than or equal to 20, print {name}, you are allowed to vote
# if the age is greater than or equal to 18 and the average is greater than or equal to 10, print {name}, you are allowed to vote
# 

age = int(input("input your age"))
full_name = input("input your name")

if age < 18 and int(average) == 20:
    print(f"{full_name}, is not allowed to vote")

if age >= 18 and int(average) >= 20:
    print(f"{full_name}, you are allowed to vote")

if age >= 18 or int(average) == 10:
    print(f"{full_name} you are allowed to vote")
else:
    print("You're now here")