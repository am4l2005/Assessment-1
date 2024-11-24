names = ["jake","Zac","Ian","Ron","Sam","Dave"]#list of namees givien
search_name = input("Enter the name you are looking for: ")#name to be searched

found = False
for name in names:
    if name == search_name:
        found = True
        break
if found:
    print("search_name + is in the given list")
else:
    print("search_name + is not in the given list")