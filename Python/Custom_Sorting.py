# Author: Pavan Kumar Paluri
'''
Problem Description:

You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''

# Solution
class Solution:
    def __init__(self):
        self.my_dict = {}
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # Custom Sort
        def func(log):
            id_, rest = log.split(" ", 1) # get first and second substr after 1st space 
            if rest[0].isalpha(): # If the first char of second substring is alphabet
                return (0, rest, id_)
            else:
                return(1,)
        return sorted(logs, key=func)


'''
Problem 2:
----------
# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100, Age)

participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

We want to sort the list in such a way that the student with the highest marks is in the beginning. 
In case the students have equal marks, they must be sorted so that the younger participant comes first.
'''

# Sorted fn

def fn():
	# Student: (Name, Marks, Age)
	participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
	]

	def helper_fn(student):
		return(100-student[1],student[2])
	return sorted(participant_list, key=helper_fn)

if __name__=="__main__":
	print(fn())

