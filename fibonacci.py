from time import time


def fib_static(n):
    if n <= 1:
        return n
    return fib_static(n-1)+fib_static(n-2)


dynamic_fib = {0: 0, 1: 1}


def fib_dynamic(n):
    global dynamic_fib
    if n in dynamic_fib:
        return dynamic_fib[n]
    ans = fib_dynamic(n-1) + fib_dynamic(n-2)
    dynamic_fib[n] = ans
    return ans


if __name__ == '__main__':
    n = int(input('N: '))
    try:
        start = time()
        x=fib_static(n)
        print(f'Static took {(time()-start):.2f} Seconds, result = {x}')
    except KeyboardInterrupt:
        print('skipped')
    start = time()
    x=fib_dynamic(n)
    print(f'Dynamic took {(time()-start):.2f} Seconds, result = {x}')
