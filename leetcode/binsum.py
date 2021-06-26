def solve(a: str, b: str) -> str:
    return bin(int(a, base=2)+int(b, base=2))[2:]


if __name__ == '__main__':
    print(solve('111', '1'))
