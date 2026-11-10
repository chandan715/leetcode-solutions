class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        num1=[]
        s=0
        for i in range(len(nums)):
            s=s+nums[i]
            num1.append(s)
        return num1

        