class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for st in strs:
            i = tuple(sorted(st))
            if i not in hashmap:
                hashmap[i]=[]
            hashmap[i].append(st)
        return list(hashmap.values())