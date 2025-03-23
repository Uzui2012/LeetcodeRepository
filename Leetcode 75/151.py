# 151. Reverse Words in a String
# Medium
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will 
# be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between 
# two words. The returned string should only have a single space separating the 
# words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        big = len(words) - 1
        small = 0
        while big > small:
            temp = words[big]
            words[big] = words[small]
            words[small] = temp
            big -= 1
            small += 1
        words = list(filter(("").__ne__, words))
        return " ".join(words)
        