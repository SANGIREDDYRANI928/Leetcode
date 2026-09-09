class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        set1=set(wordList)
        if endWord not in set1:
            return 0
        queue=[]
        queue.append((beginWord,1))
        while queue:
            word,steps=queue.pop(0)
            if word==endWord:
                return steps
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in set1:
                        set1.remove(new_word)
                        queue.append((new_word,steps+1))
        return 0        