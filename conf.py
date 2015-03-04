import lang
import sys

def main():
    if (len(sys.argv) == 1):
        print("This is the very start of the interactive prompt with Sentry Mate,\naka. the confessional... \n\nthere shall be arguments")
    elif (sys.argv[1] == "chat"):
        inmsg = ""
        print("Let's chat then...")
        lang.init()
        while inmsg not in lang.exitterms:
            inmsg = input('$>')
            print(lang.process(inmsg))

        print(lang.saybye())

if __name__ == "__main__":
    main()
    