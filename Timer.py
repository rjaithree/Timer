import time
import keyboard

def InputnValidation():
    while True:
        #Get user input for countdown duration
        user_input = input("Enter countdown duration in seconds: ")

        #Validate if it is right

        # 1. Remove any leading/trailing whitespace
        user_input = user_input.strip()
        
        # 2. Check if input is all digits, or a '-' followed by digits
        if (user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit())):
            seconds = int(user_input)       #typecasting
            if seconds > 0:
                return seconds
            else:
                print("Please enter a positive number.")
        else:
            print("Invalid input. Please enter a number.")


def FormatnDisplay(seconds):
    #Convert seconds to mm:ss format using % formatting
    minutes = seconds // 60     #floor division
    remaining_seconds = seconds % 60        #remainder
    return "%02d:%02d" % (minutes, remaining_seconds)


def Timer(total_seconds):
    #Main countdown function with pause/resume/cancel controls
    paused = False
    cancelled = False
    remaining_seconds = total_seconds
    
    print("\nCountdown started! Controls: p = pause, r = resume, c = cancel")
    print("Time remaining: %s" % FormatnDisplay(remaining_seconds), end="\r")
    
    while remaining_seconds > 0 and not cancelled:
        if(paused != True):
            if keyboard.is_pressed('p'):
                paused = True
                print("\nTimer Paused")

            elif keyboard.is_pressed('c'):
                cancelled = True
                print("\nTimer Cancelled")
                break
            
            time.sleep(1)       #Stop the execution for 1 minute
            remaining_seconds -= 1
            print("Time remaining: %s" % FormatnDisplay(remaining_seconds), end="\r")
        else:
            if keyboard.is_pressed('r'):
                paused = False
                print("\nTimer Resumed")
                print("Time remaining: %s" % FormatnDisplay(remaining_seconds), end="\r")

            elif keyboard.is_pressed('c'):
                cancelled = True
                print("\nTimer Cancelled")
                break
    

    if not cancelled:
        print("\nTime's up!")



secs = InputnValidation()
Timer(secs)