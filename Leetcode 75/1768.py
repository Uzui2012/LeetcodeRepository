# 1768. Merge Strings Alternately
# Easy
# You are given two strings word1 and word2. Merge the strings 
# by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional 
# letters onto the end of the merged string.
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        while word1 != "" or word2 != "":
            if word1 == "":
                output = output + word2
                break
            elif word2 == "":
                output = output + word1
                break
            output = output + word1[0]
            output = output + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        return str(output)