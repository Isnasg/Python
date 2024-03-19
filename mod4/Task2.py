def fastpower(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fastpower(a, n//2)
    else:
        return   fastpower(a, n-1)

def main():
    a, n = map(int, input().split())
    result = fastpower(a, n)
    print(result)
