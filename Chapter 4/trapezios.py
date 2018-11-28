import math

def f(x): #f(x)=sen(x)
    return math.sin(x)

def trapezios(a, b, n):
    h=abs(b-a)/n
    integral=f(a)+f(b)
    i=a+h
    integral=0
    while i < (b-h):
        integral=integral+2*f(i)
        i+=h
    integral=integral*(h/2)
    return integral

a=input("Input 'a' value: ")
b=input("Input 'b' value: ")
n=input("Input 'n' value: ")
a=float(a)
b=float(b)
n=float(n)

answer=trapezios(a,b,n)
print(f"Result with original step: {answer}\n")

answer=trapezios(a,b,n/2)
print(f"Result with half of the original step: {answer}\n")

answer=trapezios(a,b,n/4)
print(f"Result with one quarter of the original step: {answer}\n")
