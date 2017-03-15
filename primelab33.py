from math import sqrt,floor
from functools import reduce
from operator import mul
import matplotlib.pyplot as plt
import os

os.system('cls')

#docstring function
def doc():
    print("""

       ***   PRIMELAB   ***   
        primality functions
           v. 3/15/2017
    
    factor(n)   * Lists the factors of  n. 

    isprime(i)  * Determines if i is prime
                   * print lines of python for computation

    sieve(l)    * Sieve of Eratosthenes. Lists all primes up to limit l
    """)
    return
doc()

#Outputs a list of the smallest factors of n
def factor(n):
    data=n
    factors=[]
    #if n is negative, it is transformed into a positive number
    if data <0:
        # if n is negative, assume it positive
        print("negative conversion taking place")
        factor(-(data))
        return
    #if n is 0, it has infinite factors
    if data ==0:
        #if n is 0
        factors.append(0)
        #print(factors)
        print("Every integer is a factor of zero")
        return factors

    #determines if n is a perfect square of a square greater than 3
    upperbound=floor(sqrt(data))
    #recursively solves for factors of the square
    if upperbound > 3 and upperbound*upperbound==data:
        factors.extend(factor(upperbound))
        data=upperbound

    #if n is even, divide n by 2 until 2 is no longer a factor
    while data%2==0:
        if data==2:
            factors.append(2)
            break
        else:
            factors.append(2)
        data/=2
    #divide n by 3 until 3 is no longer a factor
    while data%3==0:
        if data==3:
            factors.append(3)
            break
        else:
            factors.append(3)
        data/=3

    jump=2
    upperbound=floor(sqrt(n))
    #determines if any prime between 5 and the square root of n are factors of n
    for s in range(5,n,jump):
        while data%s==0:
            if data==s:
                factors.append(s)
                break
            else:
                factors.append(s)
            data/=s
        
        if jump==4:
            jump=2
        elif jump==2:
            jump=4

        if reduce(mul,factors,1)==n:
            break

    #if the only factor if n is itself
    if int(data)==n:
        if n != 2 and n != 3:
            factors.append(int(data))
        factors.append(1)

    #sorts factor list
    factors.sort()

    #removes a 1 from factors list if function enters recursive square-finding loop
    if len(factors) > 2 and factors[0]==1:
        factors.pop(0)
    #print(factors)
    return factors

prompt="Lines of code for computation: "

#determines if the input is prime and lists the lines required for computation
def isprime(i):
    jump=2
    upperbound=floor(sqrt(i))
    if i%2==0:
        print(i,"is an even number! \n", prompt,'4')
        return
    if i%3==0:
        print(i,"is divisible by 3! \n", prompt ,'5')
        return
    if upperbound**2==i:
        print("The input is also the perfect square of",upperbound,"\n",prompt,'6')
        return
    lines=6
    for n in range(5,upperbound,jump):
        if i%n==0:
            print("The lowest factor is",n)
            lines+=5
            print("Lines of code for computation",lines)
            break
        else:
            if jump==4:
                jump=2
            elif jump==2:
                jump=4
        lines+=5
    else:
        print("That is a prime number!")
        lines+=4
        print("Lines of code for computation",lines)
    return

#Lists all primes up to limit l
def sieve(l):
    composite = []
    prime = []
    for i in range(2, l+1):
        if i not in composite:
            prime.append(i)
            for j in range(i*i, l+1, i):
                composite.append(j)

    #console output
    prime.sort()
    print(prime)

    #plotting
    plt.plot(prime)
    plt.title('Prime Number Distribution')
    plt.ylabel('Numbers')
    plt.xlabel('Primes before the Number')
    plt.grid()

    plt.show()
    return

