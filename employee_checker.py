COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the " + COMPANY_NAME + " employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- " + emp_name)
print("\n")

accept = ""
while accept == "":
    accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ").strip().lower()
if accept.startswith("y"):
    name = input("What is your name?\nName: ")
    for emp_name in EMPLOYEES:
        if name == emp_name:
            print("Thank you " + emp_name + ", you are now checked in.")
            break
    else:
        print("You're not an employee")
if accept.startswith("n"):
    print("This service is not for you. Exiting program...")

