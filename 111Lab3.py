#JERDON HELGESON
#111 LAB3

#TASK1
#BCS SCORE
def calc_harris_score(s):
    x = s/2850
    return x
    

def calc_coaches_score(s):
    return s/1475

def calc_bcs_score():
    harris = int(input("Enter the team’s Harris Poll ranking (1-2850): "))
    coach = int(input("Enter the team’s Coaches Poll ranking (1-1475): "))
    comp = float(input("Enter the team’s computer ranking (0-1): "))
    print("")
    h = calc_harris_score(harris)
    print("Harris Poll Score: ", h)
    c = calc_coaches_score(coach)
    print("Coaches Poll Score: ", c)
    print("Computer Ranking: ", comp)
    print("")
    final = (h+c+comp)/3
    print("Resulting BCS Score: ", final)

def Task1():
    calc_bcs_score()



#TASK2
#DOOMSDAY ALGORITHM

def doomsday():
    """This algorithm calculates the doomsday"""
    year = int(input("Enter the last two digits of the year: "))
    anchor = int(input("Enter the anchor day as an integer [0=Sunday, 7=Saturday]: "))
    doom = calc_doom(year,anchor)
    print("")
    print("Doomsday = ", doom)

def calc_doom(yr, anch):
    doom = (((yr//12)+(yr%12)+(yr%12)//4)%7+anch) % 7
    return doom

def Task2():
    doomsday()


#TASK3
#BMI

kg_per_lb = 0.45359237
m_per_inch = .0253

def bmi():
    w = float(input("Enter Weight [pounds]: "))
    h = float(input("Enter Height [inches]: "))
    h = convert_height(h)
    m = convert_weight(w)
    bmi = calc_bmi(h,m)
    print("BMI    = ", bmi )
    print("Mass   = ", m, "kg")
    print("Height = ", h, "m")

def convert_height(h):
    return h * m_per_inch

def convert_weight(w):
    return w * kg_per_lb

def calc_bmi(height, mass):
    bmi = mass/(height**2)
    return bmi

def Task3():
    bmi()

#TASK4
#Student Loan Calc



def calc_monthly_pymt(P,i, num_Months):
    print("within calc_monthly_payment")
    print("P: ",P )
    print("i: ", i)
    print("num_Months: ", num_Months)
    i2 = i /100
    num = P * (i2/12)
    den = 1 - (1+ i2/12)**-120
    p = num/den
    print("montlhy payment (p): ",p)
    return p
    
def Task4():
    P = float(input("Enter the amount you owe [no commas]: ")) #loan principal
    #print("P: ",P )
    i = float(input("Enter the interest rate [%]: ")) #interest rate
    #print("i: ", i)
    years = int(input("Enter the number of years you want to pay back the loan: "))
    #print("years: ", years)
    num_Months = years*12
    p = calc_monthly_pymt(P,i, num_Months)
    total_pay = num_Months * p
    total_int = total_pay - P
    print()
    print('Your monthly payment is $%0.2f' % p)
    print('The total amount you ended up paying is $%0.2f' % total_pay)
    print('The total amount of interest you paid is $%0.2f' % total_int)


#TASK 5
#Reverse the order of a 4 digit int

def reverse_order(number):
    print(number % 10, end="")           # Print one's place digit.
    print((number // 10) % 10, end="")   # Print 10's place digit.
    print((number // 100) % 10, end="")  # Print 100's place digit.
    print((number // 1000) % 10)         # Print 1000's place digit.
    return



    
