def r_factorial(n):
    if n == 0:
        return 1
    return n * r_factorial(n-1)


def i_factorial(n):
    answer = 1
    for item in range(n, 0, -1):
        answer *= item
    return answer
