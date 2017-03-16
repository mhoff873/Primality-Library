from math import sqrt,floor
from functools import reduce
from operator import mul
import os

os.system('cls')

#docstring function
def doc():
    print("""

       ***   PRIMELAB   ***   
           Mason Hoffman
        primality functions
           v. 3/15/2017
    
    factor(n)   * Lists the factors of  n. 

    isprime(i)  * Determines if i is prime
                   * print lines of python for computation

    sieveOfEratosthenes(l, plot=0)    * Sieve of Eratosthenes.
                   * Lists all primes up to limit l
                   * Slow, ancient sieve for finding primes
                   * plot=1 to plot with matplotlib

    sieveOfAtkin(l,plot=0)   *Sieve of Atkin
                  * Lists all primes up to limit l
                  * Modern sieve. Completes in linear time
                  * plot=1 to plot with matplotlib
    """)
    return
doc()

#Outputs a list of the smallest factors of n
def factor(n):
    data=n
    factors=[]
    #if n is negative, it is transformed into a positive number
    if data <0:
        print("negative conversion taking place")
        factor(-(data))
        return
    #if n is 0, it has infinite factors
    if data ==0:
        factors.append(0)
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
    #jump is intially 2. First it jumps from 5 to 7
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
        # adjusts jump to go between primes (5,7,11,13,17,19...)
        if jump==4:
            jump=2
        elif jump==2:
            jump=4
        #if it finds all the factors before hitting the uppperbound, break from loop
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

# Sieve of Eratosthenes
# Ancient sieve for finding primes
# Lists all primes up to limit l
def sieveOfEratosthenes(l, plot=0):
    composite = []
    prime = []
    for i in range(2, l+1):
        if i not in composite:
            prime.append(i)
            for j in range(i*i, l+1, i):
                composite.append(j)

    #plotting prime distribution
    if(plot):
        primeDistributionPlot(prime)
    #returns a list of prime numbers
    return prime

# Sieve of Atkin
# A more modern sieve for finding primes
# Works much faster than the Sieve of Eratosthenes
def sieveOfAtkin(l,plot=0):
    prime = [2,3]
    sieve=[False]*(l+1)
    for i in range(1,int(sqrt(l))+1):
        for j in range(1,int(sqrt(l))+1):
            n = 4*i**2 + j**2
            if n<=l and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*i**2+j**2
            if n<= l and n%12==7 : sieve[n] = not sieve[n]
            n = 3*i**2 - j**2
            if i>j and n<=l and n%12==11 : sieve[n] = not sieve[n]
    for i in range(5,int(sqrt(l))):
        if sieve[i]:
            for j in range(i**2,l+1,i**2):
                sieve[j] = False
    for p in range(5,l):
        if sieve[p] : prime.append(p)
    #plotting prime distribution
    if(plot):
        primeDistributionPlot(prime)
    #returns a list of prime numbers
    return prime

#Function to plot prime number distribution
def primeDistributionPlot(values):
    import matplotlib.pyplot as plt
    plt.plot(values)
    plt.title('Prime Number Distribution')
    plt.ylabel('Numbers')
    plt.xlabel('Primes before the Number')
    plt.grid()
    plt.show()
    return
