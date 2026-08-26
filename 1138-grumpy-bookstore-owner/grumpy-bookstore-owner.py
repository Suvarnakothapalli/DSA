class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        sC = 0
        n = len(customers)
        k = minutes
        for i in range(n):
            if grumpy[i] == 0:
                sC += customers[i]

        windowS = 0

        for i in range(k):
            if grumpy[i] == 1:
                windowS += customers[i]

        maxWS = windowS

        for right in range(k,n):

            if grumpy[right] == 1:
                windowS += customers[right]

            left = right - k

            if grumpy[left] == 1:
                windowS -= customers[left]

            maxWS = max(maxWS,windowS)

            

        return sC + maxWS
        