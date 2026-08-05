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
        for each in paragraph + " ":
            if each not in delimiters:
                newword += each
            else:
                if newword != "" and newword not in banned:
                    worddict[newword] = worddict.get(newword, 0) + 1
                newword = ""     
        #if newword != "" and newword not in banned:
        #    worddict[newword] = worddict.get(newword, 0) + 1
            
        return max(worddict, key=worddict.get)
    