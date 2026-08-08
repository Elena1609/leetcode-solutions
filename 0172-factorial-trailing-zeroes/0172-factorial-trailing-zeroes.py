class Solution(object):
    '''
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact = self.fact(n)
        count = 0
        while not fact%10:
            fact /=10
            count +=1
        return count    

    
    def fact(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.fact(n-1)
    '''
    def trailingZeroes(self, n):
        count = 0
        
        while n > 0:
            n = n // 5
            count += n
        
        return count    