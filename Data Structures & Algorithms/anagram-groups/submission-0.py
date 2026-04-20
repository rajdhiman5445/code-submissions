class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group  = {}
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key_count = tuple(count)
            if key_count in group:
                group[key_count].append(s)
            else:
                group[key_count] = [s]
        return list(group.values())