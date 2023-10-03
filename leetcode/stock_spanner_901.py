class StockSpanner:
    def __init__(self):
        self.stack = []
        self.prices = []

    def next(self, price: int) -> int:
        answer = 1

        while self.stack and price >= self.prices[self.stack[-1]]:
            self.stack.pop()
        if self.stack:
            answer = self.stack[-1]

        self.prices.append(price)

        return answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

solution = StockSpanner()
answer = solution.next(100)
print(answer)
assert answer == 1

answer = solution.next(80)
print(answer)
assert answer == 1

answer = solution.next(60)
print(answer)
assert answer == 1

answer = solution.next(70)
print(answer)
assert answer == 2

answer = solution.next(60)
print(answer)
assert answer == 1

answer = solution.next(75)
print(answer)
assert answer == 4

answer = solution.next(85)
print(answer)
assert answer == 6
