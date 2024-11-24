#Maping days in the month to the number of days
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}
#Ask the user to input the month number
month = int(input("Enter the month number (1-12): "))
#Verify if the input is correct before displaying the count of days.
if month in days_in_month:
    print("The total days of the month", month, "is", days_in_month[month])
else :
    print("Invalid month number please input a number between 1 an 12.")