def f(x): #f(x)=x³-3 ; zero em ~(1.441,0)
    return x*x*x-3

def corda(a, b, iterations):
    a=int(a)
    b=int(b)
    iterations=int(iterations)
    for i in range(0,iterations):
        guess=(a*f(b)-b*f(a))/(f(b)-f(a))
        if f(a)*f(guess) < 0:
            b=guess
        else:
            a=guess
        print(f"a:{a} ; b:{b} ; guess:{guess} ; i:{i}\n")
    return guess

#main:
a = input("Input a value: ")
b = input("Input b value: ")
i = input("Input how many iterations: ")

answer=corda(a,b,i)

print(f"\na:{a} ; b:{b} ; answer:{answer}\n")
