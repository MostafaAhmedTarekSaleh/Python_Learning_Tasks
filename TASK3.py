#Shopping List Tracker

shopping_list = []
repeat = True


print("Welcome to Shopping List Tracker")

while(repeat):
    print("\n(1) Add items to shopping list\n(2) Remove items\n(3) Print list")
    state = input("\nPress enter option number to proceed: ")
    if state == "done":
        print("Exiting program...")
        repeat = False
    elif state == "1":
        item = input("Input item name to be added: ")
        if item in shopping_list:
            print("\nItem already on shopping list")
        else:
            shopping_list.append(item)
            print("item added successfully +")
    elif state == "2":
        item = input("Input item name to be removed: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print("item removed successfully -")
        else:
            print("Item not present on shopping list")
    elif state == "3":
        print("Your shopping list contains: ")
        for item in shopping_list:
            print(item)

