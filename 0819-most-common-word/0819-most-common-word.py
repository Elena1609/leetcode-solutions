class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        newword = ""
        wordlist = []
        worddict = {}
        banned = set(banned)
        for each in paragraph:
            if each not in [" ","!","?","'",",",";","."]:
                newword = newword + each.lower()
            else:
                if newword != "":
                    wordlist.append(newword)
                    newword = ""   
        if newword != "":
            wordlist.append(newword)
        print wordlist      
        for word in wordlist:
            if word not in banned:
                if worddict.get(word) is not None:
                    worddict[word]+=1
                else:
                    worddict[word]=1     
        return max(worddict, key=worddict.get)
    