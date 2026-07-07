class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            hashmap=[0]*26
            for letter in s:
                hashmap[ord("a")-ord(letter)]+=1
            for letter in t:
                hashmap[ord("a")-ord(letter)]-=1
        return hashmap==[0]*26
            