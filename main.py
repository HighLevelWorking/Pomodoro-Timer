#Pomodoro timer
import time
import os

type_of_setting = input("Do you want to use a premade setting or make a custom one? (p for premade and c for custom): ").lower()
Count = True

while Count == True:
    if type_of_setting == "p":
        user_choice = int(input("Press 1 for a 60 minute work session and a 10 minute rest in between each session..." \
        "Press 2 if you want a 30 minute work session with a 5 minute break in between: "))
        if user_choice == 1:
            seconds_past = 3600
            break_time = 600
            break
        elif user_choice ==2:
            seconds_past = 1800
            break_time = 300
            break
    elif type_of_setting == "c":
        workTime = input("Please enter the number of hours or minutes you want the timer to go on for: (End the number with either m for minutes or h for hours: )")
        unit = workTime[-1].lower()
        number = workTime[:-1]       
        if number.isdigit():
            if unit == "h":
                seconds_past = int(number) * 3600
                break_time = int(input("Enter break time in minutes: ")) * 60
                break
            elif unit == "m":
                seconds_past = int(number) * 60
                break_time = int(input("Enter break time in minutes: ")) * 60
                break
            else:
                print("Invalid unit. Use 'm' for minutes or 'h' for hours.")
        else:
            print("Please enter a valid number before the unit.")
else:
    print("You can only give p or c as your input")
    


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    user_choice = input("Do you want to start the timer: (yes/no) ").lower()
    if user_choice == "yes":
        print("Your timer has started")
        for z in range(0,8):
            clear_screen()
            print("------------------------------- Work Time -------------------------------")
            for i in reversed(range (0 , seconds_past)):

                hours = i // 3600
                minutes = (i % 3600) // 60
                seconds = i % 60
                formated_Time = f"{hours:02}:{minutes:02}:{seconds:02}"
                print(f"{formated_Time:<10}", end="\r")
                time.sleep(1)
            clear_screen()
            print("------------------------------- Break Time -------------------------------")
            for x in reversed(range (0 , break_time)):

                hours = x // 3600
                minutes = (x % 3600) // 60
                seconds = x % 60
                formated_Time = f"{hours:02}:{minutes:02}:{seconds:02}"
                time.sleep(1)
                print(f"{formated_Time:<10}", end="\r")

    elif user_choice == "no":
        print("Your timer wont start")
        break
    else:
        print("You can only give yes or no as your input...")


