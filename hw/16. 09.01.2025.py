def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    elif n > 2:
        return f(n -1) ** f(n - 3) - f(n - 2)
print(f(5))
