# Validate Subsequence 
# Author: Pavan Kumar paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Validate%20Subsequence
# Time Complexity: O(N) {N:length of the array} and Space Complexity: O(N)for storing in queue

####### Approach 1: Queues #########
from collections import deque
def isValidSubsequence(array, sequence):
    # Write your code here.
    q_seq = deque(sequence)
	for num in array:
		if len(q_seq)>0 and num == q_seq[0]:
			q_seq.popleft()
	return True if len(q_seq)==0 else False
  
