# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    balance_of_savings = float(input('Enter savings account balance? '))
    interest_of_savings = float(input('Enter APR for the savings account? '))
    maturity_of_savings = int(input('Enter length of months to calculate the interest? '))


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(balance_of_savings, interest_of_savings, maturity_of_savings )

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print('The earned interest earned is: $', format(interest_earned,))
    print('The new savings account balance after',maturity_of_savings'months is: $', format(updated_savings_balance,',.2f'))


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('Enter your initial CD account balance? '))
    cd_interest = float(input('Enter APR for the CD account? '))
    cd_maturity = int(input('Enter length of months for your CD? '))


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print('earned interest on the CD is: $', format(interest_earned, ',.2f'))
    print('new CD account balance after',cd_maturity,'months is: $', format(updated_cd_balance, ',.2f'))


if __name__ == "__main__":
    # Call the main function.
    main()