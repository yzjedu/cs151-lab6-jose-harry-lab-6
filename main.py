# Programmers: Harry Li, Jose
# Course:  CS151 sec 06
# Due Date: 10/15/2024
# Lab Assignment: ATM Program
# Problem Statement: Write a program for an ATM
# Data In: User inputs the letter to the coordinated actions
# Data Out: The program outputs the balance of the user

# Output a description of the program
print('In this program it would be an ATM that includes deposit, withdraw, displaying balance and exit.')
print('The program uses "D" for deposit, "W" for withdraw, "V" for view balance,and "E" for exit.')

# Import math module
import math 
# Create variables needed
balance = 1000.00 

# Create function for deposit
def deposit_func():
    deposit = int(input('Enter the amount you want to deposit:'))
    while deposit < 0:
        deposit = int(input('Enter a valid amount:'))
    balance += deposit
    
# Create function for asking input
def action_func():
    action = input('Please enter one of the following D, W, V, or E:')
    while action != 'd' and action != 'w' and action != 'e' and action != 'v':
        action = str(input('PLEASE ENTER ONE OF THE FOLLOWING D, W, V, or E:'))

# Create function for withdraw
def withdraw_func():
    withdraw = int(input('Enter a negative number that you want to withdraw:'))
    while withdraw > 0:
        withdraw = int(input('Enter a valid amount:'))
    balance += withdraw

# Create function for checking if going into debt
def debt_func():
    if balance < 0:
        interest_fee = input('Your going to be in debt and a 5% interest fee would be charged, do you still want to proceed:')
        while interest_fee != 'no' and interest_fee != 'yes':
            interest_fee = input('Please enter yes or no:')
        if interest_fee == 'yes':
            balance *= 1.05
        else:
            balance += abs(withdraw)

# Create function for viewing balance
def view_balance():
    print('Your balance is $',balance)

# Prompt user to input D, W, V, or E and set it to the lower case form 
action = input('Please enter one of the following D, W, V, or E:')
action = action.lower()

# Check if user input is valid
while action != 'd' and action != 'w' and action != 'e' and action != 'v':
    action = str(input('PLEASE ENTER ONE OF THE FOLLOWING D, W, V, or E:'))

# While user enters 'd' give the action to deposit an amount and add to the total balance
while action == 'd':
    deposit_func()
    action = input('Please enter one of the following D, W, V, or E:')
    while action != 'd' and action != 'w' and action != 'e' and action != 'v':
        action = str(input('PLEASE ENTER ONE OF THE FOLLOWING D, W, V, or E:'))

while action == 'w':
    withdraw = int(input('Enter a negative number that you want to withdraw:'))
    while withdraw > 0:
        withdraw = int(input('Enter a valid amount:'))
    balance += withdraw
    if balance < 0:
        interest_fee = input('Your going to be in debt and a 5% interest fee would be charged, do you still want to proceed:')
        while interest_fee != 'no' and interest_fee != 'yes':
            interest_fee = input('Please enter yes or no:')
        if interest_fee == 'yes':
            balance *= 1.05
        else:
            balance += abs(withdraw)
    action = input('Please enter one of the following D, W, V, or E:')
    while action != 'd' and action != 'w' and action != 'e' and action != 'v':
        action = str(input('PLEASE ENTER ONE OF THE FOLLOWING D, W, V, or E:'))

# Output balance when user enters 'v'
while action == 'v':
    print('Your balance is $',balance)
    action = input('Please enter one of the following D, W, V, or E:')
    while action != 'd' and action != 'w' and action != 'e' and action != 'v':
        action = str(input('PLEASE ENTER ONE OF THE FOLLOWING D, W, V, or E:'))  
            
# If user enters 'E' end program 
if action == 'e':
    print('Thank you for using our ATM!')
            
            
    
