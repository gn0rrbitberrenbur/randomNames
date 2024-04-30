import random

gender = input("Generate male (m) or female (f) name? (m/f)")

if gender == 'm':
    maleForename = random.choice(list(open('NameFiles/MaleNames.txt')))
    maleLastname = random.choice(list(open('NameFiles/LastNames.txt')))
    print(maleForename.rstrip('\n')+ " " +maleLastname.rstrip('\n'))

elif gender == 'f':
    femaleForename = random.choice(list(open('NameFiles/FemaleNames.txt')))
    femaleLastname = random.choice(list(open('NameFiles/LastNames.txt')))
    print(femaleForename.rstrip('\n')+ " " +femaleLastname.rstrip('\n')) 

elif gender != 'm' or 'f':
    print("Please input your gender by pressing (m) or (f)")