def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True


n = int(input())

primes = []

# find all primes in a given range
for i in range(1, n+1):
    if is_prime(i):
        primes.append(i)

count_primes = len(primes)

# print them as pyramid
for row in range(count_primes):
    for i in range(1, primes[row]+1):
        if i in primes:
            print(1, end='')
        else:
            print(0, end='')
    print()
