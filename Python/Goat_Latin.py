# Leetcode- Easy
# Author: Pavan Kumar Paluri
# Goat Latin Problem

class Solution:
    def toGoatLatin(self, S: str) -> str:
        # first split the string 
        vowels = {'a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'}
        list_words = list(S.split())
        for i in range(len(list_words)):
            if list_words[i][0] in vowels:
                list_words[i] += "ma"
            else:
                # remove the first character from the first word of the list 
                remove_char = list_words[i][0]
                list_words[i]=list_words[i][1:]
                list_words[i]+= remove_char
                list_words[i]+= "ma"
            list_words[i]+= 'a'*(i+1)
        final_sentence = ""
        for words in list_words:
            final_sentence += words
            final_sentence += " "
        return final_sentence.rstrip(" ") 
