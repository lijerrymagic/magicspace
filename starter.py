import sys

if len(sys.argv) == 1:
    print("Welcome! Here u find a ultimate software for updating exoplanets.\n")
    print("For more information type '\help' to start!\n")
    while 1:
        user_input = sys.stdin.readline()
        if user_input == "\help\n":
            print("Hi there!")
        else:
            print("Sorry, we cannot recognize your command. Please try again.")