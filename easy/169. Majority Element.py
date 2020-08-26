class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1

        tmp = 0
        for n in list(m.keys()):
            if m[n] > tmp:
                tmp = m[n]
                answer = n
        return answer