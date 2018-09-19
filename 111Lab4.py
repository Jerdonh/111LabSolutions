#JERDON HELGESON
#CS111 LAB 4

#TASK1
#Calculate a base and exponent then find number of digits in result
def task1():
    """this will act as my task1 main()"""
    j = int(input("Enter the base j:"))
    k = int(input("Enter the exponent k:"))
    l,m = calculate(j,k)
    print(j,"**",k,"=",l,sep = "")
    print("This number has ", m, " digits.", sep = "")

def calculate(j,k):
    l = j**k
    m = len(str(l))
    return l,m
    

#TASK2
#Write a go() function to say go Team! with optional team name
def task2():
    """this will act as my task2 main()"""
    go()

def go(name = "Cougs"):
    print("Go ",name ,"!",sep = "")

#TASK3
#Find sum of digits in a 5 digit integer and the sum of that sum
def task3():
    """this will act as my task3 main()"""
    x = int(input("Enter an integer up to 5 digits long:"))
    sum_digits(x)
    

def sum_digits(num):
    n1 = num
    f1, num = divmod(num,10000)
    f2, num = divmod(num,1000)
    f3, num = divmod(num,100)
    f4, num = divmod(num,10)
    s1 = f1+f2+f3+f4+num
    print("sum of digits", n1,":",s1)
    f1,num = divmod(s1,10)
    s2 = f1+num
    print("sum of digits", s1,":",s2)
    

#TASK4
#Madlib generator
def task4():
    verb = get_sent_part('verb')
    noun1 = get_sent_part('noun')
    noun2 = get_sent_part('noun')
    noun3 = get_sent_part('noun')
    noun4 = get_sent_part('noun')
    adj1  = get_sent_part('adjective')
    adj2  = get_sent_part('adjective')
    adj3  = get_sent_part('adjective')
    madlib = build_sentence(verb, noun1, noun2, noun3, noun4, adj1, adj2, adj3)
    print(madlib)


def get_sent_part(part):
    '''
    Function to prompt user for a noun, verb, adjective, or adverb.
    '''
    print('Please enter a ', part, ':', sep='')
    part = input()
    return part

# Define a function to build sentence from user's words and rest of original
# sentence.

def build_sentence(v, n1, n2, n3, n4, adj1, adj2, adj3):
    '''
    Function to create a Mad Libs sentence with user input.
    '''
    sent = "A " + n1 + ' was an undead ' + n2 + ', usually an incredibly powerful ' + n3 + ' or king who had employed ' + adj1 + ' magic to ' + v + ' his ' + n4 + ' to his own ' + adj2 + ' corpse, thus achieving a ' + adj3 + ' form of immortality.'
    return sent

# Define main().
