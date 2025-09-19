import sys
import re
def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("none")
        return
    
    keyword, text = args

    matches = re.findall(re.escape(keyword), text)
    if not matches:
        print("none")
    else:
        print(len(matches))

if __name__ == "__main__":
    main()