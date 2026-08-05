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
        for each in paragraph:
            if each not in delimiters:
                newword = newword + each.lower()
            else:
                if newword != "" and newword not in banned:
                    if worddict.get(newword) is not None:
                        worddict[newword]+=1
                    else:
                        worddict[newword]=1
                newword = ""     
        if newword != "":
            if worddict.get(newword) is not None:
                worddict[newword]+=1
            else:
                worddict[newword]=1
            
        return max(worddict, key=worddict.get)
    