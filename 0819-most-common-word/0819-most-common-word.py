class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        newword = ""
        worddict = {}
        banned = set(banned)
        delimiters = " !?',;."
        paragraph = paragraph.lower()
        letters = []
        for each in paragraph + " ":
            if each not in delimiters:
                #newword += each
                letters.append(each)
            else:
                newword = "".join(letters)
                if newword != "" and newword not in banned:
                    worddict[newword] = worddict.get(newword, 0) + 1
                #newword = ""
                letters = []                 
        return max(worddict, key=worddict.get)
    