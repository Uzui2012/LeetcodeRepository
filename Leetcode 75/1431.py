# 1431. Kids With the Greatest Number of Candies
# Easy
# There are n kids with candies. You are given an integer array 
# candies, where each candies[i] represents the number of candies 
# the ith kid has, and an integer extraCandies, denoting the number 
# of extra candies that you have.
# Return a boolean array result of length n, where result[i] is true if, after 
# giving the ith kid all the extraCandies, they will have the greatest number 
# of candies among all the kids, or false otherwise.
# Note that multiple kids can have the greatest number of candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = 0
        for candy in candies:
            if candy > most:
                most = candy
        result = []
        for candy in candies:
            if extraCandies + candy >= most:
                result.append(True)
            else:
                result.append(False)
        return result