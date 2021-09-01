class Solution:
    def isPalindrome(self, x):
        if x<0 or x%10 == 0 and x!=0:
            return False
        revert_number = 0

        while x>revert_number:
          revert_number =revert_number*10 + x%10
          x =x//10
          print('x={},revert_number={}'.format(x,revert_number))
        if x==revert_number or x ==revert_number//10:
            return True
        return False

if __name__ == '__main__':
    data=1010
    solution = Solution()
    res = solution.isPalindrome(data)
    print(res)

