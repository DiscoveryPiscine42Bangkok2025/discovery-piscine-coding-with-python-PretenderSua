import sys
def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("none")
        return

    param = args[0]
    
    user_input = input("What was the parameter? ")
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()