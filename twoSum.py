class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # ***** Sol 01: From Discussion *****
        
        # for a number (a), (target-a) would be a pair
        dic = {}
        for i, num in enumerate(nums):
            if num in dic: 
                """if a number shows up in the dictionary already that means the necesarry pair has been iterated on 
                previously e.g. if target is 9 and if 7 is already in dic then it means its pair i.e. 2 was iterated previously """
                return [dic[num], i] # no more checking b/c of unique soln
            else:
                dic[target - num] = i 
                # Storing the 2nd element of pair along with index of first element 
                
        # ***** Sol 2: Self *****
        
        # Time = O(n^2), Space = O(n)
        # Time limit exceed
        
        indicesArr = []        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    indicesArr.extend([i,j])
        return indicesArr