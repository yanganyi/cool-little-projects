import math
import time

def si(l):
    p = [True] * (l + 1)
    p[0], p[1] = False, False
    for i in range(2, int(math.sqrt(l)) + 1):
        if p[i]:
            for j in range(i * i, l + 1, i):
                p[j] = False
    ps = [i for i, pr in enumerate(p) if pr]
    return ps

def se(low, high):
    l = int(math.sqrt(high)) + 1
    ps = si(l)
    
    p = [True] * (high - low + 1)
    if low == 1:
        p[0] = False

    for prime in ps:
        start = max(prime * prime, low + (prime - low % prime) % prime)
        for j in range(start, high + 1, prime):
            p[j - low] = False

    sepr = [i for i, prime in enumerate(p, start=low) if prime]
    return sepr

l = 1
r = l + 16500000
start_time = time.time()
primes = se(l, r)
end_time = time.time()

print(f"Number of primes found: {len(primes)}")
print(f"Time taken: {end_time - start_time} seconds")