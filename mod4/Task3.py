def euclidean_algorithm(a, b):
    if b == 0:
        return a
    return euclidean_algorithm(b, a % b)

a, b = map(int, input().split())
result = euclidean_algorithm(a, b)
print(result)