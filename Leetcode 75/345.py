# 345. Reverse Vowels of a String
# Easy
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower 
# and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        big = len(s) - 1
        small = 0
        s = list(s)
        while big > small:
            while not self.isVowel(s[small]):
                small += 1
                if small >= big:
                    return ''.join(s)
            while not self.isVowel(s[big]):
                big -= 1
                if big <= small:
                    return ''.join(s)
            temp = s[small]
            s[small] = s[big]
            s[big] = temp
            small += 1
            big -= 1
            
        return ''.join(s)

    def isVowel(self, c):
        match c:
            case 'A':
                return True
            case 'a':
                return True
            case 'E':
                return True
            case 'e':
                return True
            case 'I':
                return True
            case 'i':
                return True
            case 'O':
                return True
            case 'o':
                return True
            case 'U':
                return True
            case 'u':
                return True
            case _:
                return False
