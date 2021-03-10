# Find the Tournament Winner
# Author: Pavan Kumar Paluri
# AlgoExpert Question: https://www.algoexpert.io/questions/Tournament%20Winner
# TC: O(N) and SC: O(k) - k: number of competition languages

import operator
import math
from collections import defaultdict
def tournamentWinner(competitions, results):
    # Write your code here.
	hash_map = defaultdict(int)
	for i in range(0, len(competitions)):
		if results[i] == 0: # away team won
			hash_map[competitions[i][1]] += 3
			hash_map[competitions[i][0]] += 0
		else: # home team won
			hash_map[competitions[i][0]] += 3
			hash_map[competitions[i][1]] += 0
	# if here: tournament finished	
	max_val = -math.inf
	max_vals_key = ""
	for key, val in hash_map.items():
		if val > max_val:
			max_val = val
			max_vals_key = key
	return max_vals_key
