# Primelab
Functions for finding prime numbers, factors, and prime number distributions.

 - Written for Python 3.3. Matplotlib required to plot prime number distribution in sieves

## Functions
factor(n) 
- Lists the factors of n. 
____________________________________ 
isprime(i)
 - Determines if i is prime
 - Prints lines of code needed for computation
____________________________________  
sieveOfEratosthenes(l,plot=0)
 - Sieve of Eratosthenes. 
 - A slow, ancient sieve to find primes up to limit l
 - plot=1 plots prime number distribution in matplotlib
____________________________________  
sieveOfAtkin(l,plot=0) 
 - Sieve of Atkin. 
 - A modern sieve that completes much faster than the Sieve of Eratosthenes
 - plot=1 plots prime number distribution in matplotlib
