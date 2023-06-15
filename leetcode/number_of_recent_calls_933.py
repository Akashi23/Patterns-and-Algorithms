class RecentCounter:
    def __init__(self):
        self.recent_requests = []
        self.request_count = 0

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)
        first = self.recent_requests[0] if len(self.recent_requests) > 0 else 0

        while t - 3000 > first:
            first = self.recent_requests.pop(0)
            if t - 3000 <= first:
                self.recent_requests.insert(0, first)
                break
                
            self.request_count -= 1

        self.request_count += 1
        print(self.recent_requests)
        return self.request_count

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(2)
obj.ping(3)
obj.ping(4)
obj.ping(5)
obj.ping(4000)
obj.ping(4001)
param_1 = obj.ping(4002)

print(param_1)