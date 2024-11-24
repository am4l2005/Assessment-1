#Ask the user questions
answer = input("what is the captial of france? ")
#Evaluate the answer and it should ignore any form of capitalization
if answer.lower() =="paris":
    print("Correct!")
else:
    print("Wrong! nice try , the correct answer is Paris.")