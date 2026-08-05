class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word=""
        worddict = {}
        banned = set(banned)
        delimiters = " !?',;."
        paragraph = paragraph.lower()
        letters = []
        for each in paragraph + " ":
            if each not in delimiters:                
                letters.append(each)
            else:
                word = "".join(letters)
                if word != "" and word not in banned:
                    worddict[word] = worddict.get(word, 0) + 1
                letters = []                 
        return max(worddict, key=worddict.get)
    