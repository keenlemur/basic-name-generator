# A basic name generator by Justin Vastola

import random

print("(Press Ctrl + C to quit.)")

print(" ")

# 1. INITIALIZE VARIABLES AND LISTS
# Initialize vowels
vowelInitial = "a e i o u"
vowel = vowelInitial.split()

# Initialize consonants
consonantInitial = "b d f g h j k l m n p r s t v y z sh ch st"
consonant = consonantInitial.split()

# Initialize empty list for first and last name
# This will be appended with syllables
FNlist = []
LNlist = []


# 2. WHILE LOOP FOR FIRST AND LAST NAME
while True:

    # Ask for the first name
    while True:
        try:
            FNsyllables = int(input("Please enter first name syllables: "))
        except ValueError:
            print("Error! Please enter a valid integer, like '2'.")
            continue

        if FNsyllables < 0:
            print("Error! Your response must not be negative. Please try again.")
            continue

        else:
            break

    i = 0
    while i < FNsyllables:

        FNcombo = (random.choice(consonant) + random.choice(vowel))
        FNlist.append(FNcombo)
        i += 1

    # Ask for the last name
    while True:
        try:
            LNsyllables = int(input("Please enter last name syllables: "))
        except ValueError:
            print("Error! Please enter a valid integer, like '2'.")
            continue

        if LNsyllables < 0:
            print("Error! Your response must not be negative. Please try again.")
            continue
        else:
            break

    i = 0
    while i < LNsyllables:
        LNcombo = (random.choice(consonant) + random.choice(vowel))
        LNlist.append(LNcombo)
        i += 1


    # 3. JOIN FIRST AND LAST NAME LISTS
    # Join first and last name lists into single lists so they appear as words
    FNstring = ''.join(FNlist)
    LNstring = ''.join(LNlist)


    # 4. FIRST AND LAST NAME POSSIBILITIES 
    # Different possibilities of first and last names
    # [1:] removes the first letter
    # [:-1] removes the last letter

    # (ex. Duna)
    FNposs1 = FNstring.capitalize()
    LNposs1 = LNstring.capitalize()

    # (ex. Dunas)
    FNposs2 = FNstring.capitalize() + random.choice(consonant)
    LNposs2 = LNstring.capitalize() + random.choice(consonant)

    # (ex. Una)
    FNposs3 = FNstring[1:].capitalize()
    LNposs3 = LNstring[1:].capitalize()

    # (ex. Unas)
    FNposs4 = FNstring[1:].capitalize() + random.choice(consonant)
    LNposs4 = LNstring[1:].capitalize() + random.choice(consonant)

    # Combine possibilities into lists
    FNposs = [FNposs1, FNposs2, FNposs3, FNposs4]
    LNposs = [LNposs1, LNposs2, LNposs3, LNposs4]

    # For loop to print possibilities
    for x in FNposs:
        for y in LNposs:
            print(x, y)


    # 5. CLEAR FIRST AND LAST NAME LISTS
    # Clear first and last name lists before the while loop starts again
    FNlist.clear()
    LNlist.clear()