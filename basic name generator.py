# A basic name generator by Justin Vastola

import random

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

    # normal possibility (consonant + vowel pattern)
    poss1 = FNstring.capitalize() + " " + LNstring.capitalize()

    # possibilities where the first letter (consonant) is removed
    poss2 = FNstring[1:].capitalize() + " " + LNstring.capitalize()
    poss3 = FNstring.capitalize() + " " + LNstring[1:].capitalize()
    poss4 = FNstring[1:].capitalize() + " " + LNstring[1:].capitalize() 

    # possibiliies where the last letter (vowel) is removed and a vowel is added at the beginning
    poss5 = (random.choice(vowel) + FNstring[:-1]).capitalize() + " " + LNstring.capitalize()
    poss6 = FNstring.capitalize() + " " + (random.choice(vowel) +  LNstring[:-1]).capitalize()
    poss7 = (random.choice(vowel) +  FNstring[:-1]).capitalize() + " " + (random.choice(vowel) + LNstring[:-1]).capitalize()

    print(" ")

    print(poss1)
    print(poss2)
    print(poss3)
    print(poss4)
    print(poss5)
    print(poss6)
    print(poss7)

    print(" ")


    # 6. CLEAR FIRST AND LAST NAME LISTS
    # Clear first and last name lists before the while loop starts again
    FNlist.clear()
    LNlist.clear()