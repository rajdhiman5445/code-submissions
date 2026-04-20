class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # this removed the basic simple cases

        smap, tmap = {}, {} # two dictionaries

        for i in range(len(s)): # used the fact both s and t are of same length
            smap[s[i]] = 1 + smap.get(s[i], 0) # if this already exists then increment it else make it 1
            tmap[t[i]] = 1 + tmap.get(t[i], 0)

        return smap == tmap 