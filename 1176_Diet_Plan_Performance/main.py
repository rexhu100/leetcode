"""
A dieter consumes calories[i] calories on the i-th day.

Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for
all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] +
calories[i+1] + ... + calories[i+k-1]):

If T < lower, they performed poorly on their diet and lose 1 point;
If T > upper, they performed well on their diet and gain 1 point;
Otherwise, they performed normally and there is no change in points.

Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for
calories.length days.

Note that the total points can be negative.
"""
from typing import List
from Solution import Solution


def diet_plan_performance(calories: List[int], k, lower, upper) -> int:
    n = len(calories)
    cur = sum(calories[:k])
    point = 0
    for i in range(k, n + 1):
        if cur > upper:
            point += 1
        elif cur < lower:
            point -= 1

        cur -= calories[i - k]
        if i < n:
            cur += calories[i]

    return point


def main():
    sol = Solution()

    calories = [1, 2, 3, 4, 5]
    k = 2
    lower = 1
    upper = 4

    print(diet_plan_performance(calories, k, lower, upper))
    print(sol.dietPlanPerformance(calories, k, lower, upper))

    calories = [1, 2, 8, 4, 5, 0, 9, 34, 2, 4,56, 4, 5, 3, 4, 5, 5, 43, 37, 4]
    k = 2
    lower = 2
    upper = 10

    print(diet_plan_performance(calories, k, lower, upper))
    print(sol.dietPlanPerformance(calories, k, lower, upper))

    calories = [1, 2, 8, 4, 5, 0, 9, 34, 2, 4,56, 4, 5, 3, 4, 5, 5, 43, 37, 4]
    k = 2
    lower = 100
    upper = 1000

    print(diet_plan_performance(calories, k, lower, upper))
    print(sol.dietPlanPerformance(calories, k, lower, upper))



if __name__ == "__main__":
    main()