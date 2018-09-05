#Lab2 task1

#Parsing 4 digit num

def parse(x):
    d,rem = divmod(x,1000)
    c,rem = divmod(rem,100)
    b,a = divmod(rem,10)
    print(d,"\n",c,"\n",b,"\n",a,"\n")


def getint():
    i = int(input("Enter a positive, four-digit integer: "))
    
    return i;

def task1():
    num = getint()
    parse(num)


#Lab2 task2

#calculator

def calculator():
    c = input("Enter an arithmetic expression: ")
    print(c," = ",eval(c))

def task2():
    calculator()

#Lab2 task3

#display float as $$$

def display():
    d = float(input("Enter a decimal number: "))
    d = round(d,2) #round to two decimal places
    d = d*100 #shift decimals so they can be divmodded
    dollars, cents = divmod(d,100)
    dimes, pennies = divmod(cents,10)
    print("$",int(dollars),".",int(dimes),int(pennies),sep = "")

def task3():
    display()

#Lab2 Task4

#doomsday calculator

def doomsday(yr, anchr):
    #Doomsday=(((yr//12)+(yr%12)+(yr%12)//4)%7+anchor) %7
    doom = (((yr//12)+(yr%12)+(yr%12)//4)%7+anchr) %7
    return doom
    
def task4():
    y = int(input("Enter the last two digits of the year: "))
    a = int(input("Enter the anchor day as an integer [0 = sunday, 7 = saturday]: "))
    doom = doomsday(y,a)
    print("Doomsday = ", doom)
    
    
    
