def check_even_odd(number):
    if number % 2 == 0:#too check if the number is even or odd
        return str(number) + " is even."
    else:
        return str(number) + " is odd."
def main():
    num = int(input("Enter a number :"))#asking for the number
    
    result = check_even_odd(num)
    print(result)

if __name__ == "__main__":
    main()