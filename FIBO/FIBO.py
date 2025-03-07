memo = {0:0, 1:1}

def fibonacci(n):
    if n in memo:
        return memo[n]

    value = fibonacci(n-1) + fibonacci(n-2)

    memo[n] = value

    return value

s = int(input())

print (fibonacci(s))
