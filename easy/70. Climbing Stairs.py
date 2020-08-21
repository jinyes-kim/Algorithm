class Solution:
    def climbStairs(self, n: int) -> int:
        answer = [1, 2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            for a in range(3, n+1):
                answer.append(answer[a-2] + answer[a-3])

        return answer[n-1]