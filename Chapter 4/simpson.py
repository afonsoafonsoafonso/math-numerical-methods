import math

def f(x): #f(x)=sen(x)
    return math.sin(x)

def simpson(a, b, n):
    h=abs(b-a)/n
    integral=f(a)+f(b)
    i=1
    integral=0
    while i<n:
        if i%2==0: 
            integral=integral+2*f(a+i*h)
        else:
            integral=integral+4*f(a+i*h)
        i+=1
    integral=integral*(h/3)
    return integral

a=input("Input 'a' value: ")
b=input("Input 'b' value: ")
n=input("Input 'n' value: ")
a=float(a)
b=float(b)
n=float(n)

answer=simpson(a,b,n)
print(f"Result with original step: {answer}\n")

answer=simpson(a,b,n/2)
print(f"Result with half of the original step: {answer}\n")

answer=simpson(a,b,n/4)
print(f"Result with one quarter of the original step: {answer}\n")