from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        saved_asteroids = []

        saved_asteroids.append(asteroids[0])
        asteroids.pop(0)

        while asteroids:
            asteroid = asteroids.pop(0)
            saved_asteroid = saved_asteroids.pop()
            if saved_asteroid < 0 and asteroid < 0 or saved_asteroid > 0 and asteroid > 0:
                saved_asteroids.append(saved_asteroid)
                saved_asteroids.append(asteroid)
            elif abs(saved_asteroid) > abs(asteroid):
                saved_asteroids.append(saved_asteroid)
            elif abs(saved_asteroid) < abs(asteroid):
                asteroids.insert(0, asteroid)


        return saved_asteroids


solution = Solution()
answer = solution.asteroidCollision([5, 10, -5])
print(answer)
assert answer == [5, 10]

answer = solution.asteroidCollision([10,2,-5])
print(answer)
assert answer == [10]