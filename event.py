def askForInput(y):
    y.usrIn = input("Enter a command. Enter h for help...\n")

    while y.usrIn == "h":
        print("s    |   Stop maze rendering")
        print("start|   Start maze rendering")
        print("q    |   Quit out of program")
        print("cS   |   Change size")
        print("cW   |   Change wall size")
        print("cP   |   Change path height")
        y.usrIn = input()  

    print("input exit\n")
