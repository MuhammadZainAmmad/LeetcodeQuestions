class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        
        # My 1st accepted soln 
        # Time = O(n), Space = O(1)
        
        noOfOccurrence = nums.count(val)
        for i in range(noOfOccurrence):
            nums.remove(val)
        return len(nums)               # not necessary but decreasing runtime
        
        
        
        # From Dicussion (even worst then my soln)
        
        # while val in nums:
        #     nums.remove(val)