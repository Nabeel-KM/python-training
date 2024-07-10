def calculate_seconds(days):
    calculate_seconds_var = 24 * 60 * 60
    print(f"The seconds in {days} days are: {days * calculate_seconds_var} seconds")

def calculate_minutes(days):
    calculate_minutes_var = 24 * 60
    print(f"The minutes in {days} days are: {days * calculate_minutes_var} minutes")

def calculate_hours(days):
    calculate_hours_var = 24
    print(f"The hours in {days} days are: {days * calculate_hours_var} hours")

def choice_calculation(choice, days):
    if choice == 1:
        calculate_seconds(days)
    elif choice == 2:
        calculate_minutes(days)
    elif choice == 3:
        calculate_hours(days)
    else:
        print("Select a valid option")

def validation(number_of_days):
    try:
        days = int(number_of_days)
        if days > 0:
            return True
        else:
            print("Enter a valid number of days")
            return False
    except ValueError:
        print("Enter a valid number of days")
        return False
    
to_continue = True

while to_continue:
    days_input = input("\nNo of days: ").split()
    choice = int(input("1. Seconds \n2. Minutes \n3. Hours \n\nEnter the choice: "))

    for number_of_days in days_input:
        if validation(number_of_days):
            choice_calculation(choice, int(number_of_days))
        else:
            print("Wrong Input")
    
    user_choice = input("\nDo you want to continue (y/n): ").strip().lower()
    if user_choice == 'n':
        to_continue = False
