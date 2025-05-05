# a = 4
# b = 2
# c = 1
# average= (a+b+c)/3
# print(average)

def average(num1, num2, num3):
    d =(num1+num2+num3)/3.0
    print(d)

average(2,4,6)
average(3,5,8)

def average(num1, num2, num3):
    avg=(num1+num2+num3)/3.0
    return avg
    
avg=average(4,3,5)
print(avg)

# default values
def sum(a, b=5):
    print(a+b)

sum(5)

# Keyword Argument
def studentinfo(name, age):
    print(f"Name:{name}, Age:{age}")
studentinfo(age=3, name="Sauarav")

#lambda function
square = lambda x: x*x
print(square(2))
sq=square(5)
print(sq)

sum=lambda x,y: x+y
print(sum(5,5))

#fibonacii series means addition of previous two number we get new number

""" 
 values     0    1  1   2   3   5   8   13
indexes     0   1   2   3   4   5   6   7 
    
fib(0)=0
fib(1)=1
fib(2)=fib(1)+fib(1)
fib(3)=fib(1)+fib(2)
fib(4)=fib(2)+fib(3)


"""
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2) + fib(n-1)

print(fib(2))

"""
fib(6)=fib(4)-fib(5)


"""

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2) + fib(n-1)
print(f"Fibonacii value for : {fib(2)}")