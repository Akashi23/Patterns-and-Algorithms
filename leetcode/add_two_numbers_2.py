# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        iterator1 = LinkedListIterator(l1)
        iterator2 = LinkedListIterator(l2)
        resultIterator = LinkedListIterator(ListNode(0))

        while True:
            if iterator1.current == None and iterator2.current == None and carry == 0:
                break

            if iterator1.current == None and iterator2.current == None and carry == 1:
                resultIterator.current.next = ListNode(1)
                print("here")
                break

            if iterator2.current == None:
                summary, carry = self.sum(
                    iterator1.current.val, 0, carry)

                iterator1.current = iterator1.current.next
                resultIterator.current.next = ListNode(summary)
                resultIterator.current = resultIterator.current.next
                continue

            if iterator1.current == None:
                summary, carry = self.sum(
                    0, iterator2.current.val, carry)

                iterator2.current = iterator2.current.next
                resultIterator.current.next = ListNode(summary)
                resultIterator.current = resultIterator.current.next
                continue

            summary, carry = self.sum(
                iterator1.current.val, iterator2.current.val, carry)

            resultIterator.current.next = ListNode(summary)

            resultIterator.current = resultIterator.current.next
            iterator1.current = iterator1.current.next
            iterator2.current = iterator2.current.next

        return resultIterator.head.next

    def sum(self, digit1: int, digit2: int, carry: int) -> int:
        summary = digit1 + digit2 + carry
        if summary > 9:
            return summary - 10, 1
        return summary, 0


class LinkedListIterator:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            temp = self.current
            self.current = self.current.next
            return temp


def printLinkedList(l: Optional[ListNode]):
    if l == None:
        print("None")
    else:
        print(l.val)
        printLinkedList(l.next)


solution = Solution()
answer = solution.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(
    9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
printLinkedList(answer)
