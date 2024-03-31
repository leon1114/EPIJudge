from test_framework import generic_test


def fibonacci(n: int) -> int:
    # TODO - you fill in here.

    pp, p = 0,1
    if n <= 1:
        return n

    tmp = 2
    while tmp <= n:
        pp, p = p, p + pp
        tmp += 1

    return p


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
