""" A program that allows the user to access two different financial calculators: 
an investment calculator and a home loan repayment calculator. """

import math

def get_valid_number(input_message):
    """Function to get a valid float number from user input."""
    while True:
        try:
            return float(input(input_message))
        except ValueError:
            print("Error! Please enter a valid number. \n")

def get_valid_integer(input_message):
    """Function to get a valid integer from user input."""
    while True:
        try:
            return int(input(input_message))
        except ValueError:
            print("Error! Please enter a valid number.\n")

# Display menu for the user to choose between investment and bond
print("""
Finance Calculator
Welcome! Which financial calculator would you like to use?:

Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a home loan
""")

# Get the user's choice and ensure it is either 'investment' or 'bond'
while True:
    user_choice = input("Enter [investment] or [bond] to proceed: ").lower()
    print("")

    if user_choice in ['investment', 'bond']:
        break  # Exit the loop if a valid choice is provided
    else:
        print("Error! Please try again.")

if user_choice == 'investment':
    # Get user input for investment calculation
    deposit = get_valid_number("Enter the amount you are depositing: £")
    interest_rate = get_valid_number("Enter the interest rate (Please enter a number only): ")
    years = get_valid_integer("Enter the number of years you plan on investing: ")
    interest_type = input("Which interest type would you be using?: [simple] or [compound] ").lower()

    # Divide interest rate by 100
    interest_rate /=  100

    # Perform calculations based on the type of interest
    if interest_type == 'simple':
        total_amount = deposit * (1 + interest_rate * years)
    elif interest_type == 'compound':
        total_amount = deposit * math.pow((1 + interest_rate), years)

    # Display the results
    print("_________________________________________________\n")
    print(f"In {years} years, your total amount will be: £{total_amount:.2f}")
    print("_________________________________________________")

elif user_choice == 'bond':
    # Get user input for bond calculation
    value_of_house = get_valid_number("Enter the present value of the house: £")
    interest_rate = get_valid_number("Enter the interest rate (Please enter a number only): ")
    months = get_valid_integer("Enter the number of months you plan to repay the bond back by: ")

    # Divide interest rate by 100
    interest_rate /= 100

    # Calculate monthly interest and bond repayment
    monthly_interest = interest_rate / 12
    repayment = (monthly_interest * value_of_house) / (1 - (1 + monthly_interest) ** (-months))

    # Display the results
    print("______________________________________________\n")
    print(f"Your monthly bond repayments will be: £{repayment:.2f}")
    print("______________________________________________")