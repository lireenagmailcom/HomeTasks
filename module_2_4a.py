
# numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
primes = [2, 3, 5, 7]  # список primes содержащий только простые числа.
not_primes = []  # список not_primes, содержащий все не простые числа.
n = int(input('Enter number: '))
print(n)
for j in primes:
    print(n, j, n/j)
    if n % j == 0:
        not_primes.append(n)

    primes.append(n)

print(primes)
print(not_primes)