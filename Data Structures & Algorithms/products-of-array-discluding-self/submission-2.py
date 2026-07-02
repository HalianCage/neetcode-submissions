class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        Algorithm :-
        Step 1: Initialize two arrays each for left product and right product of each element
        Step 2: In a single for loop, 
            for left product:
                - If is first element, add 1 into leftProdArray
                - If not, multiply i-1 of leftProdArray with i-1 of nums array
            for right product:
                - Start with len(nums)-i-1
                - If last element, add 1 to rightProdArray
                - If not, multiply len(nums)-i of rightProdArray with len(nums)-i of nums array
        Step 3: Multiply leftProdArray and rightProdArray element for element, store in an array and return the output.
        '''

        length = len(nums)
        leftProdArray = [0] * length
        rightProdArray = [0] * length

        for i in range(length):

            # leftProdArray
            if i == 0:
                leftProdArray[i] = 1
            else:
                leftProdArray[i] = leftProdArray[i-1] * nums[i-1]


            # rightProdArray
            invert = length-1-i
            if i == 0:
                rightProdArray[invert] = 1
            else:
                rightProdArray[invert] = rightProdArray[invert+1] * nums[invert+1]

        return [leftProdArray[i] * rightProdArray[i] for i in range(length)]

        