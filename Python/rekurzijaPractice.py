#1. Compute the Factorial of a number N. F act(N) = N × (N −1)· · · 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#2. Compute the sum of natural numbers until N.

def sumOfNaturalNums(n):
    if n == 1:
        return 1
    else:
        return n + sumOfNaturalNums(n-1)

#3. Write a function for mutliply(a, b), where a and b are both positive integers, but you can only use the + or − operators.

def multiply(a,b):
    if b == 0:
        return 0 
    else:
        return a + multiply(a, b-1)

#5. find the greatest common divisor

def gcd(x , y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
        
#6. Obrni niz

def obrniR(niz):
    if niz == "":
        return niz
    else:
        return obrniR(niz[1:]) + niz[0]
"""
def kvadrat(vnos):
    for i in range(len(vnos)):
        vrstica = ""
        for j in range(len(vnos)):
            if(i<=j and i+j<=len(vnos)-1 or i>=j and i+j>=len(vnos)-1):
                vrstica += "1 "
            else:
                vrstica += "0 " 
        print(vrstica)
"""

def kvadrat(vnos):
    for i in range(len(vnos)):
        vrstica = ""
        for j in range(len(vnos)):
            if(i+j<=len(vnos)-1 and i>=j):
                vrstica += "1 "
            else:
                vrstica += "0 " 
        print(vrstica)





def nekajCudnega(niz):
    izhod = niz
    for i in range(len(niz)):
        izhod = izhod[i:] + izhod[:i]
        print(izhod)

kvadrat("kodadadaa")
