# print("Welcome to the Grow Program")

# Request user to input their name

# first_nam = input("What is first name?\n")
# last_nam = input("What is last name?")


# Print Welcome message with user's name

# print(name)

# print("You're welcome", name,",we are glad to have you")

# print(f"Welcome, {first_nam} {last_nam} ")


# Ask  user to enter first number
# first_number = input("Input a first number \n")

# # and ask user to enter second number
# second_number = input("Input a second number \n")

# # add the two numbers

# # first_number = int(first_number)
# # second_number = int(second_number)

# sum = int(first_number) + int(second_number)


# answer = first_number + second_number

# # add the 2 numbers and print the results

# print(sum)



# # Ask user to enter first name
# first_name = input("What is your first name \n")

# # ask user to enter their last name
# last_name = input("What is your last name \n")
# # print user's full name in UPPERCASE.

# fullname = f"{first_name} {last_name}"

# # user = fullname.upper()

# print(fullname.upper())


# if else


# age = input("How old are you?\n")

# if int(age) >= 18 and int(age) <= 35: # 18 <= int(age) <= 45
#     print("you can have acess")
# else:
#     print("you are not allowed")

# age = input("How old are you?\n")

# if 18 <= int(age) and 45 <= int(age): # 18 <= int(age) <= 45
#     print("you can have acess")
# else:
#     print("you are not allowed")


# Program 1.

# ask user to input a integer
# number = input("Input a number")

# # determine the modulo of the integer

# new = int(number) % 2
# # if the modulo is equall to 2, print even

# if new == 0:
# # else print odd
#     print("even")
# else:
#     print("odd")




# Ask user to input their score as a number

# if score is between 90 to 100(inclusive) print grade A

# if score is between 80 to 89(inclusive) print grade B

# if score is between 70 to 79(inclusive) print grade C

# if score is between 60 to 69(inclusive) print grade D

# if score is between 0 to 59(inclusive) print grade F

# score = int(input("Enter your Exam Score\n"))

# if score >= 90 and score <= 100:
#     print("Grade A")

# if score >= 80 and score <= 89:
#     print("Grade B")

# if score >= 70 and score <= 79:
#     print("Grade C")

# if score >= 60 and score <= 69:
#     print("Grade D")

# if score >= 0 and score <= 59:
#     print("Grade F")
# else:
#     print("Please input Correct grade")



# Ask user to input their Purchase amount as float
# if the purchase is 100gh or more, apply a discout of 20% and print amount to pay
# if the purchase is 50gh or more, apply a discount of 10% and print amount to pay
# if the purchase is less than 50gh apply no discount and print amount to pay


# purchase_amount = float(input("What is your Purchase Amount\n"))

# big_discount = purchase_amount * 0.2

# small_discount = purchase_amount * 0.1

# # new_purchase_amount = purchase_amount - discount

# if purchase_amount >= 100:
#     print(purchase_amount - big_discount)

# elif purchase_amount >= 50 and purchase_amount <= 99:
#     print(purchase_amount - small_discount)
# else:
#     print(purchase_amount)

# ask user to input the 3 sides triangle
# x = float(input("Enter the first side: "))
# y = float(input("Enter the Second side: "))
# z = float(input("Enter the Third side: "))

# # if all sides are equall, print Equilateral
# if x == y == z:
#     print("Equilateral")
# # if two sides are equall, print isosceles
# elif x == y or y == z or z == x:
#     print("Isosceles")
# # if no sides are equall, print scalene
# else:
#     print("Scalene")

# file = open("tasks.txt",)
# tasks = file.read().split("\n")
# for task in tasks:
#     print(f"{tasks.index(task)}. {task}")

# use loop to calculate the sum of the numbers below

# numbers = [10, 5, 20, 8, 15]

# for num in numbers:
#     num = sum (numbers)
# print(nu)


# total = 0
# for num in numbers:
#     total = total + num
# print(total)


# file = open("emails.txt")
# emails = file.read().split("\n")
# for email in emails:
#     name = email.split("@")[0]
#     print(f"Your Username is: {emails.index(name)}. {name}")

# for username in file:
#     if username == "@":
#         break
# print(username)

# define a register user function
# def register_user(name, email, password):
#     # check if user does not already exist
#     # hash user password
#     # validate input
#     # check if user is not a bot
#     # return response
#     return "User registered successfully!"

# response = register_user("nana", "something@gmail.com", "123232")
# import add
# import show
# import update
# import delete

# add_task_repsponse = add.add_task("Sleep")
# print(add_task_repsponse)

# show_tasks_response = show.show_tasks()
# print(show_tasks_response)

# update_task_response = update.update_task("sleep", "Wake up")
# print(update_task_response)

# delete_task_response = delete.delete_task("Wake up")
# print(delete_task_response)

from oop import Chat

chat_with_abena = Chat()
print(chat_with_abena)
