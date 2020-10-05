# Complement of Base 10 integer
# Author: Pavan Kumar Paluri

# Gvien a number find its 10's complement and return it as an integer

class Solution:
  def bitwiseComplement(self, N:int)->int:
      num_bits = 0
      str_num = bin(N)
      str_num = str_num.replace("0b","")
      num_bits = len(str_num)
      num = 2**(num_bits)-1
      return N^num
 
 if __name__=="__main__":
    sol = Solution()
    print(sol.bitwiseComplement(10))
    
