print('Welcome to the CareerDevs employee check-in')

careerdevs = ["Keith", "Manny", "Rodney", "Kat"]
accept = input("Do you work for CareerDevs?\n(yes/no): ")
if accept == "yes":
    name = input("What is your name?\n")
    for emp_name in careerdevs:
        if name == emp_name:
            print("Okay, you're an employee!")
            break
    else:
        print("You're not an employee!")

else:
    print ("Okay, you can leave!!")

    print("whatever")


