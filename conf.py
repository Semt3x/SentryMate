import lang
import sys

def main():
    version = "0.2a"
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
    elif (sys.argv[1] == "help"):
        print("SentryMate v"+version+"\nValid arguments are :\n - help : displays this help\n - chat : enjoy a nice chat with your personnal sentry")

if __name__ == "__main__":
    main()
    