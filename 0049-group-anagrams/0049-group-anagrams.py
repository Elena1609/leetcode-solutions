class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map = {}
        for word in strs:
            word_sorted = tuple(sorted(word))
            if word_sorted not in hash_map:
                hash_map[word_sorted] = [word]
            else:
                hash_map[word_sorted].append(word)    

        return hash_map.values()