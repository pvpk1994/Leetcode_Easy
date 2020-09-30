# verifying an alien dictionary 
# Author: Pavan Kumar Paluri
# O(NlogN) for sorting 

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def func(st):
            list_ret = []
            for character in st:
                if character in order:
                    list_ret.append(order.index(character))
            return list_ret
        words_new = sorted(words, key=func)
        return words_new==words
        
