class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        obj={}
        for i in nums:
            if i not in obj:
                obj[i]=1
            else:
                obj[i]+=1
        maxi=0
        for i in obj:
            if obj[i]>maxi:
                maxi=obj[i]
                key=i
        return key
        