def f(x): #f(x)=x³-3 ; zero em ~(1.441,0)
    return x*x*x-3

def df(x): #df(x)=f'(x)=3x²
    return 3*x*x

def newton(guess,iterations):
    guess=int(guess)
    iterations=int(iterations)
    for i in range(0,iterations):
        guess=guess-f(guess)/df(guess)
        print(f"guess:{guess} ; i:{i}\n")

#main
x0 = input("Input x0 value: ")
i = input("Input how many iterations: ")

newton(x0,i)
