# 1, 1, 2, 3, 5, 8, 13

fibonacci = [1, 1]

for i in range(10):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)