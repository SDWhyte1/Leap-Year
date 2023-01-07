checkAgain = True
while checkAgain:
    def leap_year(years): #functuon which checks whether a number is a leap year or not
        numberStore = 0
        numberStore2 = 0
        number3 = 0
        if years % 4 == 0 and years % 100 != 0: #and years % 400 == 0:
            numberStore = years / 4
            numberStore2 = years / 100
            numberStore3 = years / 400
            print(numberStore)
            print(numberStore2)
            print(numberStore3)
            print ("The year " +str(years) + " is a leap year")
            print("\n")
        elif years % 4 == 0 and years % 400 == 0:
            numberStore = years / 4
            numberStore2 = years / 100
            numberStore3 = years / 400
            print(numberStore)
            print(numberStore2)
            print(numberStore3)
            print ("The year " +str(years) + " is a leap year")
            print("\n")
        else:
            print("The year " +str(years) + " is not a leap year")
            print("\n")
    year = int(input("Please enter a year that you would like to check whether it is a leap year: "))
    leap_year(year)

    checkUser = input("Would you like to check anymore years (enter y or n)? ")
    if checkUser == "n":
        checkAgain = False
        print(" Over")
