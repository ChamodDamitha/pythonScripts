import time

#.....................normal method
def isPrime(x):
    n=2
    if x==0 or x==1 :return False
    while n <= x/2:
        if x%n==0:return False
        n+=1
    return True

def getPrimesOld(bound):
    primes = []
    i = 0
    while i < bound:
        if isPrime(i) :
            primes.append(i)
        i+=1
    return primes

bound = 100000
    
t1 = time.time()
primes1 = getPrimesOld(bound)
print("time elapse : " + str(time.time() - t1))
#print(primes1)

        
#............................prime sieve

def getPrimes(bound):
    prime_sieve = list(range(2, bound))
    j = 0
    while j < len(prime_sieve):
        k = j + 1
        p = prime_sieve[j]
        while k < len(prime_sieve):
            #print("k : " + str(k) + ", j : " + str(j) + "len : " + str(len(prime_sieve)))
            if prime_sieve[k] % p == 0:
                del prime_sieve[k]
            k+=1
        j+=1
    return prime_sieve

t2 = time.time()
primes2 = getPrimes(bound)
print("time elapse : " + str(time.time() - t2))
#print(primes2)

