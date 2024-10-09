#User Info
age = float(input("Enter your age:"))
membership = (input("Are you a member?(Yes/No):"))

#verifying
 
if membership == "yes" or membership== "no":
    if age >= 0 or age < 18:
        if membership == "yes":
             print("Your registration fee is 450.00 pesos.")
        elif membership == "no":
             print("Your registration fee is 650.00 pesos.") 
    elif age >= 19 or age <= 65:
        if membership == "yes":
            print("Your registration fee is 550.00 pesos.")
        elif membership == "no":
             print("Your registration fee is 750.00 pesos.") 
    elif age >= 65 or age<= 120:
        if membership == "yes":
             print("Your registration fee is 400.00 pesos.")
        elif membership == "no":
             print("Your registration fee is 600.00 pesos.") 
    else:
        print("Invalid input: Please only choose Yes or No.")
else:
   print("Invalid input.")