# age = int(input("How old are you?\n"))
age = 135
decades = age//10
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old.")

#=========================================================

temperature = 75
forecast = "sunny"

if temperature < 80 and forecast != "rainy":
    print("Go outside!")
else:
    print("Stay inside!")

#=========================================================

raining = True
if not raining:
    print("Go outside!")
else:
    print("Stay inside!")

#=========================================================

import random
roll = random.randint(1,6)
print("The computer rolled a " + str(roll))

#=========================================================

import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
# user_choice = input('Do you want rock, paper, or scissors?')
user_choice = 'rock'

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
else:
    print('You lose, computer wins :)')

#=========================================================

expenses = [10.50, 8, 5, 15, 20, 5, 3]
expenses.append(16)
print(expenses)
del expenses[3]
print(expenses)
expenses.remove(20)
print(expenses)
sum = 0
for x in expenses:
    sum = sum + x
print(sum)
print(200/10/5)

#=========================================================

menus = { 'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
          'Lunch' : ['BLT', 'PB&J', 'Turkey Sandwich'],
          'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Taco'] }
for name, menu in menus.items( ):
    print(name, ':', menu)

#=========================================================

contacts = {
'number': 4,
'students':
[
{'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
{'name': 'Harry Potter', 'email': 'harry@example.com'},
{'name': 'Hermione Granger', 'email': 'hermione@example.com'},
{'name': 'Ron Weasley', 'email' : 'ron@example.com'}
]
}
print('Student emails:')
for student in contacts['students']:
    print(student ['email'])

#=========================================================

def greeting (s):
    print('Hello', s)
# Main program
input_name = 'Shreyas'
greeting (input_name)