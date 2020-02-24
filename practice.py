
# Print your name and how many decades old you are
name = "Guido"

age = 24

def print_string():
    print(name, age)
    print(int(age/10), "decades old")

print_string()


listOfNames = ["bob", "nob", "Noble", "Boble"]
# Don't print names over 5 characters or ones that contain the letter N
def nameSorter(nameList):
    for name in nameList:
        if (len(name) <= 5) and "n" not in name and "N" not in name:
            print(name)
        else:
            continue
# Use a while loop to empty the list
    nameIndex = 0
    while len(nameList) != 0:
        nameList.pop(nameIndex)
    print(nameList)

nameSorter(listOfNames)