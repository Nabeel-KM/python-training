import os
import datetime

def check_cpu(command):
    print(os.system(command))

def show_date():
    return datetime.datetime.today()

def check_memory(command):
    print(os.system(command))

def check_date(command):
    print(os.system(command))
    
def run_command(command):
    print(os.system(command))

today = show_date()

print(today)

check_cpu("df -h")

check_memory("free -m")

check_date("date")