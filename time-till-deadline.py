import datetime

user_input = input("Enter your goal with a deadline seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]

deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()

time_left = deadline_date - today_date
# time_left_till = str(deadline_date - today_date).split(",")

# time_left = time_left_till[0]

print(f"Dear User! Time remaining for your goal: {goal} is {time_left.days} days")