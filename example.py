def f(x):
    return 2 * x + 7

def g(x):
    return x * 2

if __name__ == "__main__":
    x = 2
    print(f(x))
    print(g(x))
    print(f(g(x)))
    print(g(f(x)))
    result = f(x) + g(x) + f(g(x)) + g(f(x))
    print(result)