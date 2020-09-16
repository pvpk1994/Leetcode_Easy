# Leetcode Question: https://leetcode.com/problems/length-of-last-word/
# Author: Pavan Kumar Paluri
# Return the length of last word with characters (upper/lowercase) 

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) ==0:
            return 0
        word_counter  =0
        list_word_count= []
        for i,character in enumerate(s):
            if character != " " and i!=len(s):
                word_counter += 1
            elif character == " " and word_counter!=0:
                list_word_count.append(word_counter)
                word_counter = 0
            if i==len(s)-1 and character != " ":
                list_word_count.append(word_counter)
        if len(list_word_count)>0 :
            return list_word_count[-1]
        else:
            return 0
