class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # From Discussion (But not a best one)
        
        lastIndx = len(digits) - 1
        while digits[lastIndx] == 9:
            digits[lastIndx] = 0
            lastIndx -= 1
        if(lastIndx < 0):
            digits = [1] + digits
        else:
            digits[lastIndx] += 1
        return digits
        
        # My 1st soln (not working for 99)
        
        # lastDigit = digits.pop()
        # if lastDigit == 9:
        #     digits.extend([1,0])
        # else:
        #     digits.append(lastDigit+1)
        # return digits