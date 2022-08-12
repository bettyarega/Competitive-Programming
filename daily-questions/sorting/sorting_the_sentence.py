class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        copy_words = words[:]
        for i in range(len(copy_words)):
            last = int(copy_words[i][-1])
            words[last-1] = copy_words[i]
        
        for j in range(len(words)):
            words[j] = words[j][:-1]
        return ' '.join(words)
    
Solution().sortSentence("is2 sentence4 This1 a3")