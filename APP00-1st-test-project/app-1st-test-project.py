whatisthisAbout = """This program calculates the percentage of marks
based upon the individual score
for a given student."""

print(whatisthisAbout + "\n\n")

'''
# Declaring variables and initializing
pointspossible = 100
studentname = input("Enter Student Name: ")

try:
    score = int(input("Enter Student Score outta {} : ".format(pointspossible)))
    print("You entered a valid integer.")
except Exception:
    print("ERROR: Please Enter an integer value for Student Score")


# Calculating the marks in percentage of total
markPercentage = (score / pointspossible) * 100
print("{} got {}% marks. ".format(studentname, round(markPercentage,2)))

if 100 >= markPercentage >= 90:
        grade = "A"
elif 89 >= markPercentage >= 80:
        grade = "B"
elif 79 >= markPercentage >= 70:
        grade = "C"
elif 69 >= markPercentage >= 60:
        grade = "D"
else:
        grade = "F"

print("His Grade is {}".format(grade))

'''

def printtype(text):
    print(type(text))

printtype(56.89)


# SETS
numbers = [3, 2, 2, 4, 5, 5, 2, 4, 9, 3, 10, 10, 1, 5, 2, 10, 1, 9, 2]
unique = set(numbers)
print(unique)

# FOR LOOP
numbers = [76, 83, 16, 69, 52, 78, 10, 77, 45, 52, 32, 17, 58, 54, 79, 72, 55, 50, 81, 74, 45, 33, 38, 10, 40, 44, 70, 81, 79, 28, 83, 41, 14, 16, 27, 38, 20, 84, 24, 50, 59, 71, 1, 13, 56, 91, 29, 54, 65, 23, 60, 57, 13, 39, 58, 94, 94, 42, 46, 58, 59, 29, 69, 60, 83, 9, 83, 5, 64, 70, 55, 89, 67, 89, 70, 8, 90, 17, 48, 17, 94, 18, 98, 72, 96, 26, 13, 7, 58, 67, 38, 48, 43, 98, 65, 8, 74, 44, 92]
newnumbers = []

for num in numbers:
    if num % 2 != 0:
        newnumbers.append(num)

print(len(newnumbers))
newnumbers = set(newnumbers)
print(newnumbers)
print(len(newnumbers
######################

# WHILE LOOP

power = 1
while 2**power < 1000000000:
    power += 1
    print(power)

# FOR LOOP ADVANCED

nums = [99, 20, 30, 35, 16, 49, 39, 11, 69, 48, 85, 32, 10, 47, 24, 80, 37, 21, 3, 99, 13, 11, 23, 12, 40, 50, 24, 14, 10, 62, 21, 24, 55, 57, 38, 55, 83, 63, 34, 31, 15, 26, 82, 47, 37, 14, 64, 72, 90, 39, 70, 50, 67, 61, 23, 28, 30, 13, 87, 58, 80, 62, 15, 49, 33, 7, 38, 2, 92, 76, 80, 18, 6, 25, 22, 25, 91, 9, 37, 83, 46, 98, 69, 3, 40, 6, 48, 1, 63, 51, 32, 19, 77, 74, 22, 75, 41, 19, 27, 82, 60, 6, 1, 55, 5, 71, 18, 84, 47, 16, 1, 8, 41, 6, 17, 100, 62, 36, 45, 32, 4, 33, 68, 15, 2, 92, 50, 54, 34, 12, 17, 16, 74, 95, 2, 61, 75, 12, 6, 39, 28, 18, 30, 39, 8, 34, 62, 31, 57, 8, 69, 19, 71, 70, 40, 79, 76, 96, 84, 76, 85, 4, 40, 64, 45, 11, 46, 100, 56, 9, 86, 5, 78, 81, 18, 70, 76, 46, 85, 69, 64, 88, 17, 91, 49, 93, 18, 29, 38, 42, 77, 63, 46, 32, 83, 88, 48, 68, 89, 80]


count = 0

for num in nums:
    if nums[count] == 68:
        break
    count += 1

print(count)

print(nums[count])

###################

## hangman game version
lives = 10
word = list("ANCHOR".lower())

print("WORD: " + str(word))
print("Length: " + str(len(word)))

newword = "_"*len(word)
newword = list(newword)

print("NEWWORD: " + str(newword) )

def somefunc():
    global lives
    lives -= 1
    print("OUCH! Lives remaining now = " + str(lives) )

somefunc()


while lives > 0:

    yourletter = input("Enter your letter: ").lower()
    print(yourletter)

    for index in range(len(word)):

        if yourletter == word[index]:
            print("You found the right letter! ")
            newword[index] = yourletter
            print("Current status is: " + str(newword) )
            lives += 1
        else:
            continue

    else:
        somefunc()

#############

## DICTIONARY STUFF
words = ["PoGo","Spange","Lie-Fi"]

definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

mydict = {}

for x in range(len(words)):
    mydict[words[x]] = definitions[x]

print(mydict)

##############
