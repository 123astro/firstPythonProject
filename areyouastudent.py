print('Welcome to the CareerDevs employee check-in.')

careerdevs = ["Keith", "Manny", "Rodney", "Kat"]
print("\nAre you a student? Lets find out...\n")
accept = ""
while accept == "":
    accept = input("Are you a student?\n(yes/no): ").strip().lower()
if accept.startswith("y"):
    name = input("What is your name?\n").strip()
    for emp_name in careerdevs:
        if name == emp_name:
            print("Welcome to the class!")
            break
    else:
        print("You're not suppose to be here!")
else:
    print ("Okay, you can leave!!")