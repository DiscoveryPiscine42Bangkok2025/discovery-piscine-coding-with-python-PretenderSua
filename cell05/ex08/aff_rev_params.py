import sys
def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("none")
    else:
        for arg in reversed(args):
            print(arg)

if __name__ == "__main__":
    main()