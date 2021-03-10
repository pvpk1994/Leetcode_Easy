# Sorted Squared Array 
# Author: Pavan Kumar Paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Sorted%20Squared%20Array
# Time Complexity: O(NlogN) Space Complexity: O(N)

def sortedSquaredArray(array):
    # Write your code here.
	return sorted([num*num for num in array])
    # return []
