class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute Force

        time: O(n^2)
        space: O(1)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        '''

        '''
        [2,7,11,15]
        1. 2
        dict = {}
        dict[ target - 2 ] = 0
        dict[ 9 - 2 ] = 0
        dict[7] = 0
        
        2. 7
        return [dict[7], 1] => [0,1]
        
        time: O(n)
        space: O(n)
        
        '''

        dict = {}
        for i, n in enumerate(nums):
            if n in dict:
                return [dict[n], i]
            dict[target - n] = i
        return []
