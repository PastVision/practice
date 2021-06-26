def solve(digits: list) -> list:
    carry = 1
    i = len(digits) - 1
    while carry:
        if i < 0:
            digits.insert(0, carry)
        else:
            digits[i] += carry
        if digits[i] > 9:
            digits[i] = 0
            i -= 1
        else:
            carry = 0
    return digits


if __name__ == '__main__':
    print(solve([9, 9, 9]))
