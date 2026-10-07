class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):    # j starts at i+1
                if nums[i] + nums[j] == target:
                    return [i, j]

l1=[3,4,6]
l2=[1,7,3]

def getNumber(l) :
    i=len(l)-1
    while i >= 0 :
        number += str(l[i])
        i-=1
    return int(number)
#643 [3,4,6]
def getList(n):


