def calculate_seconds(days):
    calculate_seconds_var = 24*60*60
    return print(f"The seconds in {days} days are : {days * calculate_seconds_var} seconds")

def calculate_minutes(days):
    calculate_minutes_var = 24*60
    return print(f"The minutes in {days} days are : {days * calculate_minutes_var} minutes")

def calculate_hours(days):
    calculate_hours_var = 24
    return print(f"The hours in {days} days are : {days * calculate_hours_var} hours")

def choice_calculation(choice,days):
    
    #days = int(days)
    if (choice == 1 ):
        calculate_seconds(days)

    elif (choice == 2 ):
        calculate_minutes(days)

    elif (choice == 3 ):
        calculate_hours(days)

    else:
        print("Select a valid option")

def validation(number_of_days):
    days = int(number_of_days)
    if (days > 0):
        return True
    elif (days == 0):
        print("Enter a valid number of days")
        return False
    else:
        print("Enter a valid number of days")
        return False
    
toContinue = True

while (toContinue):
    

    days = input("\nNo of days : ")
    print(type(days.split()))
    print(days.split())
    choice = int(input("1. Seconds \n2. Minutes \n3. Hours \n\nEnter the choice : "))

    for number_of_days in days.split():
        number_of_days = int(number_of_days)
        input_validated = validation(number_of_days)
        if input_validated:
            choice_calculation(choice,number_of_days)
        else:
            print("Wrong Input")
            continue

    

    user_choice = input("\nDo you want to continue (y/n) : ")

    if (user_choice == 'n' or user_choice == 'N'):
        toContinue = False

    