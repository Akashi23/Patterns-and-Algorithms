from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        saved_asteroids = []

        for asteroid in asteroids:
            while saved_asteroids and asteroid < 0 and saved_asteroids[-1] > 0:
                diff = asteroid + saved_asteroids[-1]
                if diff < 0:
                    saved_asteroids.pop()
                elif diff > 0:
                    asteroid = 0
                else:
                    asteroid = 0
                    saved_asteroids.pop()
            if asteroid:
                saved_asteroids.append(asteroid)

        return saved_asteroids


solution = Solution()
answer = solution.asteroidCollision([5, 10, -5])
print(answer)
assert answer == [5, 10]

answer = solution.asteroidCollision([10, 2, -5])
print(answer)
assert answer == [10]
