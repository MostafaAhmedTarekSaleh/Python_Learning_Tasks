#Simple Tip Calculator

print("Welcome to Tip Calculator ")

repeat = True
while (repeat):
    state = input("\nPress any key here to proceed or \"quit\" to exit: ")
    if state =="quit":
        print("Exiting program...")
        repeat = False
    else:
        bill = float(input("\nEnter the bill amount: "))
        tip_percentage = float(input("Please enter the desired tip %: "))

        tip = tip_percentage/100 * bill

        total = bill + tip

        print(f"Tip amount = {tip:.2f}")

        print(f"Total Bill amount = {total:.2f}")