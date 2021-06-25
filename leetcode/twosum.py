
def solution(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [i, seen[target-num]]
        seen[num] = i


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    print(solution(nums, target))
