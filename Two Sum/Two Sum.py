class Solution(object):
    def twoSum(self, nums, target):
        #iterate through all the numbers
        #by count up to the number of numbers in nums array starting at 0
        for i in range(len(nums)):
            #range(start, stop, step) (where start and step are optional arguments)
            #using the above arguments we start the second iterating because
            #we can't use the same element twice
            for k in range(i+1,len(nums)):
                #if the two current numbers equal the target
                if nums[i] + nums[k] == target:
                    #return the current numbers
                     return [i,k]
        return []