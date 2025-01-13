# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
def is_next_prime(n, primtal):
    for i in primtal:
        if n % i == 0:
            return False
    return True


primtal = [2]

for i in range(3, 10):
    if is_next_prime(i, primtal):
        primtal.append(i)

print(primtal)

