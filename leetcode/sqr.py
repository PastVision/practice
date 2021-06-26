#   0 1 2 3 4 5 6 7 8

def sqrt(x: int) -> int:
    lb = 0
    rb = x
    while lb <= rb:
        mid = (lb+rb)//2
        if mid*mid == x:
            return mid
        if mid*mid > x:
            rb = mid - 1
        else:
            lb = mid + 1
    return rb


if __name__ == '__main__':
    print(sqrt(int(input('N: '))))
