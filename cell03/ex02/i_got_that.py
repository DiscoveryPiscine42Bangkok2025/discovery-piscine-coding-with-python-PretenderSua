user_input = input("What you gotta say? : ")
if user_input != "STOP":
    while True:
        user_input = input("I got that! Anything else? : ")
        if user_input == "STOP":
            break