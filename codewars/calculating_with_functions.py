# ""
# "This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five()))    #  must return 35
# four(plus(nine()))      #  must return 13
# eight(minus(three()))   #  must return 5
# six(divided_by(two()))  #  must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))"


def zero(ls=None): 
    if ls == None:
        return '0' #your code here
    else:
        return int(eval("0" + ls))
def one(ls=None): 
    if ls == None:
        return '1' #your code here
    else:
        return int(eval("1" + ls))
def two(ls=None): 
    if ls == None:
        return '2' #your code here
    else:
        return int(eval("2" + ls))
def three(ls=None): 
    if ls == None:
        return '3' #your code here
    else:
        return int(eval("3" + ls))
def four(ls=None):
    if ls == None:
        return '4' #your code here
    else:
        return int(eval("4" + ls))
def five(ls= None): 
    if ls == None:
        return '5' #your code here
    else:
        return int(eval("5" + ls))
def six(ls=None): 
    if ls == None:
        return '6' #your code here
    else:
        return int(eval("6" + ls))
def seven(ls=None): 
    if ls == None:
        return '7' #your code here
    else:
        return int(eval("7" + ls))
def eight(ls=None): 
    if ls == None:
        return '8' #your code here
    else:
        return int(eval("8" + ls))
def nine(ls= None): 
    if ls == None:
        return '9' #your code here
    else:
        return int(eval("9" + ls))

def plus( rs): return "+ {}".format(rs) #your code here
def minus( rs ): return "- {}".format(rs) #your code here
def times( rs ): return "* {}".format(rs) #your code here
def divided_by( rs ): return "// {}".format(rs) #your code here