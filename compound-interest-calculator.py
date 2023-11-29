### Compound Interest Calculator

# Define function to get the original investment amount.
def get_value_original_amount():
    original_amount = None
    while original_amount == None:
        try:
            original_amount = float(input("""\nWhat is the amount of your investment in U.S. dollars ($)? """))
        except ValueError:
            print("""You must enter a number. You may enter a whole number or a decimal. Please do not use commas. \nPlease try again.""")
        except Exception as err:
            print("""Error:""", err)
    return float(original_amount)

# Define function to get the account interest rate.
def get_value_interest_rate():
    interest_rate = None
    while interest_rate == None:
        try:
            interest_rate = float(input("""\nWhat is the interest rate of the account? \nPlease enter the interest rate as a decimal -- If the interest rate is 2.5%, enter .025: """))
        except ValueError:
            print("""You must enter a number. Please enter the interest rate as a decimal. Please do not use commas. \nPlease try again.""")
        except Exception as err:
            print("""Error:""", err)
    return float(interest_rate)

# Define function to get the length of the investment in years.
def get_value_investment_length():
    investment_length = None
    while investment_length == None:
        try:
            investment_length = int(input("""\nHow many years long is the investment? """))
        except ValueError:
            print("""You must enter a whole number. Please do not use commas. \nPlease try again.""")
        except Exception as err:
            print("""Error:""", err)
    return float(investment_length)

# Define function to get the number of compoundings per year.
def get_value_yearly_compounding():
    yearly_compounding = None
    while yearly_compounding == None:
        try:
            yearly_compounding = int(input("""\nHow many times is the interest compounded per year? """))
        except ValueError:
            print("""You must enter a whole number. Please do not use commas. \nPlease try again.""")
        except Exception as err:
            print("""Error:""", err)
    return float(yearly_compounding)

# Define function to compute the total balance at the end of the investment period (formula for compound interest).
def compute_total_balance(original_amount, interest_rate, investment_length, yearly_compounding):
    total_balance = original_amount * (1 + (interest_rate / yearly_compounding)) ** (yearly_compounding * investment_length)
    return total_balance

# Define function to compute the amount of interest earned over time (total balance - original amount).
def compute_interest_earned(total_balance, original_amount):
    interest_earned = total_balance - original_amount
    return interest_earned

# Define function to print the results.
def print_compound_interest(investment_length, yearly_compounding, interest_rate, original_amount, interest_earned, total_balance):
    # Print the investment account information (investment length, yearly compounding, and interest rate).
    print(f"""\nYour investment is for {format(investment_length, ',.0f')} years, with {format(yearly_compounding, ',.0f')} compoundings per year, and an interest rate of {format(interest_rate, '.2%')} (rounded to 2 decimal places).""")

    # Print the original investment amount.
    print(f"""Your original investment amount is ${format(original_amount, ',.2f')}.""")

    # Print the amount of interest earned.
    print(f"""The amount of interest earned will be ${format(interest_earned, ',.2f')}.""")

    # Print the total balance of the investment at the end.
    print(f"""The total balance of your investment will be ${format(total_balance, ',.2f')}.""")


# Define main function.
def main():
    # Greet user with purpose of program.
    print("""Let's calculate your compound interest!""")

    # Call functions to get the values from the user.
    original_amount = get_value_original_amount()
    interest_rate = get_value_interest_rate()
    investment_length = get_value_investment_length()
    yearly_compounding = get_value_yearly_compounding()

    # Call functions to compute the compound interest.
    total_balance = compute_total_balance(original_amount, interest_rate, investment_length, yearly_compounding)
    interest_earned = compute_interest_earned(total_balance, original_amount)

    # Call function to print the results of the compound interest calculator.
    print_compound_interest(investment_length, yearly_compounding, interest_rate, original_amount, interest_earned, total_balance)

main()