class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        n=len(nums)
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for j in dic:
            if dic[j]>n/2:
                return j

        