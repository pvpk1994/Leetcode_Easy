# Author: Pavan Kumar Paluri
# CodeSignal Easy Problem
'''
Problem Description:
-------------------
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. 
The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. 
If it does not become a valid arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and

solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]

the output should be
isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and

solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]

the output should be
isCryptSolution(crypt, solution) = false.

Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
'''
def isCryptSolution(crypt, solution):
    # Convert solution into dictionary first
    sol_dict = {list_sol[0]:list_sol[1] for list_sol in solution}
    # print(sol_dict)
    summ = 0
    str_num_list = []
    for i in range(len(crypt)):
        str_num = ""
        for j in range(len(crypt[i])):
            if len(crypt[i])>1 and sol_dict[crypt[i][0]]=='0':
                return False 
            else:
                str_num+= sol_dict[crypt[i][j]]
        str_num_list.append(int(str_num))
    print(str_num_list)   
    if str_num_list[0]+str_num_list[1]==str_num_list[2]:            
        return True
    else:
        return False  
                
