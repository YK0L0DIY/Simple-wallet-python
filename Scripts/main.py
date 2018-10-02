#simpple wallet app done by @y.kolodiy
#for more information https://github.com/YK0L0DIY

import os


def _main_():
    base = open('base.txt', 'r+')
    action = open('actions.txt', 'a')
    try:
        balance = int(base.readline())
    except:
        balance = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    while 1:
        print("1) balance")
        print("2) add money")

        print("3) take money")
        print("4) show actions")
        print("5) exit")

        try:
            choice = int(input())
        except:
            print("Invalid input\n")


        if choice == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            printBalance(balance)

        elif choice == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                value = int(input('How many to add: '))
                balance = balance + value
                action.writelines("+  ADD  %10s EUR\n" % (value))
                printBalance(balance)
            except:
                print("Error in the value")

        elif choice == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                value = int(input('How many to take: '))
                if balance - value < 0:
                    print("Impossibel action\n")

                else:
                    action.writelines("- Take  %10s EUR\n" % (value))
                    balance = balance - value
                    printBalance(balance)
            except:
                print("Erro in the value")

        elif choice==4:
            os.system('cls' if os.name == 'nt' else 'clear')
            action.close()
            show=open('actions.txt','r')
            s=show.readline()
            while s!='':
                print(s)
                s=show.readline()
            print("==========================")
            printBalance(balance)

            show.close()


            print("0) delete info")
            print("else to continue\n")

            try:
                choice = int(input());
                if choice == 0:
                    action = open('actions.txt', 'r+')
                    action.truncate(0)
                    action.close()
                    print("deleted\n")

            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            action=open('actions.txt','a')


        elif choice == 5:
            base.seek(0)
            base.truncate()
            base.seek(0)
            base.writelines(str(balance))
            base.close()
            action.close()
            break

        else:
            print("Invalid input\n")


def printBalance(balance):
    print("TOTAL : %10s EUR" % balance, "\n")
    return


_main_()
