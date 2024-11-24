#Get input from user
name = input("Enter user name: ")
hometown = input("Enter user hometown: ")
#Ask for age and validate it to be an integer
age = input("Enter user age: ")
while not age.isdigit():
    print("Enter a valid number for age. ")
    age = input("Enter your age: ")
#Print all the values in seprate lines using a single print code
print("name: "+ name + "\nhometown: " + hometown + "\nage: " + age)