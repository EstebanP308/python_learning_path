With_ID = (input("Do you have an ID? yes/no: ")).lower()

if With_ID == "yes":
    Password = input("Enter Password: ") 

    if Password == "Onex":
        print("Access Granted") 
    else:
        print("Access Denied")
else:
    print("Access Denied")


last = input("\nPress Enter to exit...")
