temp = int(input("enter the temperature:\n\n"))
choice = input("\nenter 1 for Fahrenheit to Celcius. \nenter 2 for Celcius to fahrenheit.\n\n")
if choice == "1":
    # the flowchart says "no" in both directions lol
    print("\nthe temperature in Celcius is: " + str((5/9)*(temp-32)))
elif choice == "2":
    print("\nthe temperature in fahrenheit is: " + str((9*temp+(32*5))/5))
else:
    print("\ninvalid input")