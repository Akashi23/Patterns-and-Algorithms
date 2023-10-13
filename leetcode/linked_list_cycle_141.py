from typing import Optional


class ListNode:
    def __init__(self, x):
        self.head = None
        self.val = x
        self.next = None
        self.pos = None

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = ListNode(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(data)
        return self


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        head.pos = i
        while head.next:
            print(head.val, head.pos)
            if head.pos - i > 0:
                return False
            i += 1
            head.next.pos = i
            head = head.next

        return True


solutionData = ListNode(3).insertAtEnd(2).insertAtEnd(0).insertAtEnd(-4)
solution = Solution()
answer = solution.hasCycle(solutionData)
print(answer)
assert answer == True

solutionData = ListNode(1).insertAtEnd(2)
answer = solution.hasCycle(solutionData)
print(answer)
assert answer == True

solutionData = ListNode(1)
answer = solution.hasCycle(solutionData)
print(answer)
assert answer == False
