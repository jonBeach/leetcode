#A lot of my failed attemps were due to an extra = I had ==  instead of = :)
#I also started this one without reading properly and was making it so that
#It could make as much profit as possible and not just the one single most
#profitable answer :)
class Solution(object):
    def maxProfit(self, prices):

        #variables to keep track of the smallest and biggest numbers along with the max profit
        #I feel like I cheated a little with the profit variable because if someone asked for
        #the two numbers that made up the most profit my solution would be wrong
        smallestNumber = prices[0]
        biggestNumber = prices[0]
        profit = 0
        #Loop through all the prices starting at index of one because I already set the
        #smallest and biggest numbers to the first index of the prices array
        for i in range(1,len(prices)):
            #Checks if the current price is less than the current smallest number
            #also makes sure that it's not checking the very last number as nothing comes after
            #I could remove the check for last number as the profit variable makes it pointless
            if prices[i] < smallestNumber and i != len(prices)-1:
                #if the number is smaller make it the new smallest
                #and make the biggest current number the same
                #because no number before the current smallest number matters
                #But if i didn't use profit and someone asked for the two numbers that made up
                #the largest profit I would have to change this
                smallestNumber = prices[i]
                biggestNumber = smallestNumber
            #Checks if the current price is higher than the current biggest number
            if prices[i] > biggestNumber:
                biggestNumber = prices[i]
            #Takes the current biggest and smallest number and compares it to the previous
            #if the current profit is bigger than the last then that's the new answer
            #If it's not and none are bigger than 0 then no profit can be made
            if (biggestNumber - smallestNumber) > profit:
                profit = biggestNumber - smallestNumber
        return profit
