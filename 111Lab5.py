#JERDON HELGESON
#111 LAB5

#TASK1
#check if positive integer is even
def is_even(x):
    if(x <= 0):
        return str(x) + " is not greater than 0."
    elif(int(x)%2 == 0):
        return str(int(x)) + " is even."
    else:
        return str(int(x)) + " is odd."

#TASK2
#Returns if a year is a leap year or not

def leap_year(year):
    if(year%4 == 0):
        if(year%100 != 0):
            return True
        elif(year%400 == 0):
            return True
    else:
        return False

def task2():
    year = int(input("Enter a year[4 digits]: "))
    if(leap_year(year)):
        print(year, " is a leap year!")
    else:
        print(year, " is not a leap year.")


#TASK3
#Doomsday.. again..

def set_anchor(yr):
    sYr = str(yr)
    if(sYr[0:2:1] == "19"):
        return 3
    elif(sYr[0:2:1] == "20"):
        return 2
    else:
        return -1

def calc_doom(yr, anchor):
    doom = (((yr // 12) + (yr % 12) + (yr % 12) // 4) % 7 + anchor) % 7
    #doom = (((yr//12)+(yr%12)+(yr%12)//4)%7+anchor) %7
    return doom
    

def task3():
    year = int(input("Enter a year in four digits: "))
    det_anchor, yr = divmod(year, 100)
    anchor = set_anchor(year)
    doom = calc_doom(yr,anchor)
    print("Doomsday = ", doom)

#TASK4
#calculate BMI

kg_per_lb = .45359237
m_per_inch = .0254

def convert_height(inches):
    """Convert inches to meters"""
    return m_per_inch * inches

def convert_weight(lbs):
    """COnvert lbs to kgs"""
    return kg_per_lb * lbs

def calc_bmi(height_m, mass):
    return mass / height_m ** 2

def classify_bmi(bmi):
    bC = "BMI Classification = "
    if(bmi <= 18.5):
        bC += "Underweight"
    elif(bmi <= 24.99):
        bC += "Normal Weight"
    elif(bmi <= 29.99):
        bC += "OverWeight"
    elif(bmi <= 34.99):
        bC += "Obesity (I)"
    elif(bmi <= 39.99):
        bC += "Obesity (II)"
    else:
        bC += "Morbid Obesity"
    return bC

def task4():
    heighti = float(input("Enter height [inches]: "))
    weightlb = float(input("Enter weight[lbs]: "))
    mHeight = convert_height(heighti)
    kMass = convert_weight(weightlb)
    bmi = calc_bmi(mHeight,kMass)
    bC = classify_bmi(bmi)
    print(bC)
    pass
    
    
