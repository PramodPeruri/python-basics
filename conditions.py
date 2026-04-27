#Python is case sensitive a and A are not same
environment = input("Enter your environment: \n")
change_ticket = False

environment = environment.casefold()

if environment == "PROD":
    change_ticket = True
    print("Please provide a change ticket")
elif environment == "staging":
    print("Welcome to staging environment")
else:
    print("Please login using your credentials")
