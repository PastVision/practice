class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(l1, l2):
    carry = 0
    for i, j in zip(l1, l2):
        print(i, j)


if __name__ == '__main__':
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    print(solution(l1, l2))
