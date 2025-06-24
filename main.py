import time
#Pomodoro timer
seconds_past = 3600



while True:
    user_choice = input("Do you want to start the timer: (yes/no) ").lower()
    if user_choice == "yes":
        print("Your timer has started")
        for z in range(0,8):
            print("------------------------------- Work Time -------------------------------")
            for i in reversed(range (0 , seconds_past)):

                hours = i // 3600
                minutes = (i % 3600) // 60
                seconds = i % 60
                formated_Time = f"{hours:02}:{minutes:02}:{seconds:02}"
                print(formated_Time, end = "\r")
                time.sleep(1)
            print("------------------------------- Break Time -------------------------------")
            for x in reversed(range (0 , 1200)):

                hours = x // 3600
                minutes = (x % 3600) // 60
                seconds = x % 60
                formated_Time = f"{hours:02}:{minutes:02}:{seconds:02}"
                time.sleep(1)
                print(formated_Time, end = "\r")

    elif user_choice == "no":
        print("Your timer wont start")
        break
    else:
        print("You can only give yes or no as your input...")


