import math

def average(x,y):
    return(x+y)/2
def square(number):
    return number*number

def sqrt_aman(number):
    def closeEnough(guess):
        return(math.fabs((square(guess))- number) < 1)
    def improve(guess):
        return average(guess,(number/guess))
    def sqrtHelper(guess):
        if(closeEnough(guess)):
            return guess
        else:
            nnum = improve(guess)
            print(nnum)
            return sqrtHelper(nnum)
    return sqrtHelper(1.0)

               
