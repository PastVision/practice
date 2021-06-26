from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display(head: ListNode):
    ptr = head
    ret = ''
    while ptr:
        ret += str(ptr.val) + ('->' if ptr.next else '')
        ptr = ptr.next
    print(ret)


def solution(l1):
    head = l1
    while l1:
        if l1.next and l1.val == l1.next.val:
            l1.next = l1.next.next
        else:
            l1 = l1.next
    return head


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(1, ListNode(1)))
    display(l1)
    display(solution(l1))
