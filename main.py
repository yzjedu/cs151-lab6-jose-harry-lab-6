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
def deposit_func(balance):
    deposit = float(input('Enter the amount you want to deposit: '))
    while deposit < 0:
        deposit = float(input('Enter a valid amount: '))
    balance += deposit
    return balance
    
# Create function for asking input
def action_func(action):
    action = input('Please enter one of the following D, W, V, or E:')
    action = action.lower()
    while action != 'd' and action != 'w' and action != 'e' and action != 'v':
        action = str(input('PLEASE ENTER ONE OF THE FOLLOWING D, W, V, or E:'))
    return action
    
# Create function for withdraw
def withdraw_func(balance):
    withdraw = float(input('Enter the amount you want to withdraw: '))
    while withdraw < 0 or withdraw > balance:
        if withdraw > balance:
            print("Insufficient balance.")
        withdraw = float(input('Enter a valid amount: '))
    balance -= withdraw

# Create function for checking if going into debt
def debt_func(balance):
      if balance < 0:
        interest_fee = input('You are in debt, and a 5% interest fee will be charged. Do you still want to proceed? (yes/no): ').lower()
        while interest_fee not in ['yes', 'no']:
            interest_fee = input('Please enter yes or no: ').lower()
        if interest_fee == 'yes':
            balance *= 1.05
        else:
            balance += withdraw  # undo withdrawal if user opts out of debt
        return balance


# Create function for viewing balance
def view_balance(balance):
    print(f'Your current balance is: ${balance:.2f}')

# Prompt user to input D, W, V, or E and set it to the lower case form 
action = input('Please enter one of the following D, W, V, or E:')
action = action.lower()

# Check if user input is valid
while action != 'd' and action != 'w' and action != 'e' and action != 'v':
    action = str(input('PLEASE ENTER ONE OF THE FOLLOWING D, W, V, or E:'))

while action != 'e':
    if action == 'd':
        balance = deposit_func(balance)
        action = action_func(action)
    if action == 'w':
        balance = withdraw_func(balance)
        balance = debt_func()
        action = action_func(action)
    if action == 'v':
        view_balance(balance)
        action = action_func(action)
    
# If user enters 'E' end program 
if action == 'e':
    print('Thank you for using our ATM!')
            
            
