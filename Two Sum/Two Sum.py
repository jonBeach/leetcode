class Solution(object):
    def twoSum(self, nums, target):

        #iterate through all the numbers
        #by count up to the number of numbers in nums array starting at 0
        for i in range(len(nums)):
            #check if the current number is greater than the target
            #because you can't add up to the target number if one
            #of the numbers is already greater than it
            if nums[i] < target:
                #range(start, stop, step) (where start and step are optional arguments)
                #using the above arguments we start the second iterating because
                #we can't use the same element twice
                for k in range(i+1,len(nums)):
                    #check if greater than target same as above
                    if nums[k] < target:
                        #if the two current numbers equal the target
                        if nums[i] + nums[k] == target:
                            #return the current numbers
                            return [i,k]
