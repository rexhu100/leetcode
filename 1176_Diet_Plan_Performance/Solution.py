class Solution(object):
    def dietPlanPerformance(self, c, k, l, u):
        temp = 0
        for i in range(k):
            temp += c[i]
        right = k - 1
        left = 0
        points = 0
        while right < len(c):
            if temp < l:
                points -= 1
            elif temp > u:
                points += 1
            temp -= c[left]
            left += 1
            right += 1
            if (right >= len(c)):
                break
            temp += c[right]
        return points
