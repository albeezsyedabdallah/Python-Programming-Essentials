def calculate_simple_interest(principal, time, gender, senior_citizen):

    if gender.lower() == "female" and senior_citizen:

        rate = 0.08

    elif gender.lower() == "female" and not senior_citizen:

        rate = 0.06

    elif gender.lower() == "male" and senior_citizen:

        rate = 0.07

    elif gender.lower() == "male" and not senior_citizen:

        rate = 0.05

    else:

        return "Invalid gender or senior citizen status."

    interest = principal * rate * time

    return interest

principal_amount = float(input("Enter the principal amount: "))

time_period = float(input("Enter the time period in years: "))

customer_gender = input("Enter the customer's gender (Male/Female): ")

senior_citizen_input = input("Is the customer a senior citizen? (yes/no): ")


senior_citizen = True if senior_citizen_input.lower() == "yes" else False

simple_interest = calculate_simple_interest(principal_amount, time_period, customer_gender, senior_citizen)

print("Simple Interest:", simple_interest)

