#Give the correct answer which is required
correct_pass = "246810"
attempts = 0
#Ask the user for the right password untill right answer is entered or till attempts runs out
while attempts < 5:
    password = input("Enter the right password: ")
    
    if password == correct_pass:
        print("Permission has been given. Valid password! ")
        break
    else:
        attempts += 1
        print("permisson denied .try again. ")
if attempts == 5:
    print("Max number of attempts has been reached. AUTHORITIES HAS BEEN ALERTED.")