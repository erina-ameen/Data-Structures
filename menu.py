while True:
    print("======= MAIN MENU =======")
    print("1. List Operations")
    print("2. Tuple Operations")
    print("3. Dictionary Operations")
    print("4. Set Operations")
    print("5. Exit")
    choice=int(input("Enter Choice: "))

    if choice==1:
        list1=[]
        while True:
            print("--- List Menu ---")
            print("1. Add Element")
            print("2. Remove Element")
            print("3. Display List")
            print("4. Back to main menu")
            choice2=int(input("Enter Choice: "))
            if choice2==1:
                choice3=input("Enter element you would like to add: ")
                list1.append(choice3)
            elif choice2==2:
                choice3=input("Enter element you would like to remove: ")
                list1.remove(choice3)
            elif choice2==3:
                print(list1)
            elif choice2==4:
                print("Returning to main... ")
                break

    if choice==2:
        tuple1=()
        while True:
            print("--- Tuple Menu ---")
            print("1. Create Tuple")
            print("2. Display Tuple")
            print("3. Count Elements")
            print("4. Back to main menu")
            choice2=int(input("Enter Choice: "))
            if choice2==1:
                choice3=input("Input elements with spaces in between: ")
                tuple1=tuple(choice3.split())
            elif choice2==2:
                print(tuple1)
            elif choice2==3:
                print(len(tuple1))
            elif choice2==4:
                print("Returning to main... ")
                break
