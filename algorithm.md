# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...

1. Output a Welcome Message Explaining the Purpose of the Program:
    Output the following:
        "This is an ATM that includes deposit, withdraw, displaying balance, and exit."
        "The program uses 'D' for deposit, 'W' for withdraw, 'V' for view balance, and 'E' for exit."
2. Initialize Variables:

    Set balance = 1000.00 (initial balance).
    Set SENTINEL = 'E' (to exit the loop).
    No need to declare choice as we handle user input directly within the loop.
3. Start a While Loop That Continues Until the User Enters 'E' to Exit:

    Display the menu options:
        D - Deposit
        W - Withdraw
        V - View Balance
        E - Exit
    Prompt the user to input their choice and convert it to lowercase.
4. Handle the User's Choice:
    If the choice is 'D' (Deposit):
        Call the deposit_func(balance) function:
          - Prompt the user to enter the amount to deposit.
          - Validate that the deposit amount is a positive number.
          - If valid, add the deposit amount to balance and return the updated balance.
          - Otherwise, continue to prompt the user until a valid amount is entered.
    If the choice is 'W' (Withdraw):
        Call the withdraw_func(balance) function:
          - Prompt the user to enter the amount to withdraw.
          - Validate that the withdrawal amount is a positive number and less than or equal to balance.
          - If valid, subtract the amount from balance.
          - If the balance becomes negative:           
              - Prompt the user with a warning message about a 5% interest charge.  
              - Ask if the user wishes to proceed with the withdrawal:
                 - If the user accepts, apply the 5% interest fee to the balance.
                 - If the user declines, reverse the withdrawal (undo it). 
          - Return the updated balance.
    If the choice is 'V' (View Balance):
          - Call the view_balance(balance) function:
                 - Output the current balance to the user.
    If the choice is 'E' (Exit):
          - Output a message thanking the user and indicating that the program is ending.
          - Break out of the loop to end the program.
    If the choice is not one of the valid options:
          - Output an error message asking the user to enter a valid option (D, W, V, or E).
5. Output a Message Indicating the ATM Program Has Ended:
          - Output "Thank you for using our ATM!" before exiting the loop when the user chooses 'E'.





