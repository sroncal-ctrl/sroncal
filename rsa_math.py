import math
import random


def primeNums(n):
    nums = [True]*n

    if n>=2:
        nums[0] = False
        nums[1] = False

    for x in range(2,math.isqrt(n)+1):
        for i in range(x*x, n, x):
            if nums[i]:
                nums[i] = False

            else:
                pass
    prime_values = [i for i, prime in enumerate(nums) if prime]

    return prime_values


    #for num in range(1,len(nums)):
        #print(f"{num}:{nums[num]}", end=" ")


def extended_gcd(a, b):
    
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y




def encrypt(message,encryption_key,pq):
    encrypted_message = pow(message, encryption_key, pq)
    return encrypted_message

def decrypt(message,decryption_key,pq):
    decrypted_message = pow(message, decryption_key, pq)
    return decrypted_message


def generate_keys(bit_size):

    #convert bits to decimal

    num_size = (2**bit_size)-1

    primeNumbers = primeNums(num_size)

    #Create a pool to choose from random values in primes list    
    primes_maxrange = len(primeNums(num_size))
    primes_minrange = len(primeNums(2**(bit_size-3)-1))

    primes_pool = primeNumbers[primes_minrange:primes_maxrange]

    #choose p and q, and if equal then choose new values until they arent

    p = random.choice(primes_pool)
    q = random.choice(primes_pool)
    while p == q:
        p = random.randint(primes_pool)
        q = random.randint(primes_pool)
    
    n = p*q

    phi_n = (p-1)*(q-1)

    #Generate a random number coprime to n:
    e = random.randint(2**(bit_size-3)-1,num_size)
    while math.gcd(e,phi_n) != 1:
        e = random.randint(2**(bit_size-3)-1,num_size)

    #Define the public key which will be returned

    public_key = (e,n)

    gcd,x,y = extended_gcd(e, phi_n)

    d = x % phi_n

    private_key = (d,n)

    return public_key, private_key




    








    

     



