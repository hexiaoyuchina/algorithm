class Solution:
    def longestPalindrome(self, strs):
        '''
        维护四个指针，left、left1、right、right1,需要知道mid位置，个数为奇偶数
        越界：
        left1<left
        '''
        s_len = len(strs)
        if len(set(list(strs)))==1:
            return strs

        for str_len in range(s_len,0,-1):#字串长度从长到短：
            for index in range(s_len):#子串的起始位置
                if index+str_len>s_len:
                    break
                child_str = strs[index:index+str_len]
                child_str_len = len(child_str)
                if child_str_len==1:
                    return child_str
                
                mid = child_str_len//2
                if child_str_len%2==0:
                    #子串为偶数
                    left = 0
                    right = mid-1                    
                    left1 = mid
                    right1 =  child_str_len-1

                else:
                    left = 0
                    right = mid-1
                    left1 = mid+1
                    right1 =  child_str_len-1

                while left<= right:
                    # print(child_str,left,right,left1,right1)
                    if child_str[left]!=child_str[right1] or child_str[left1]!=child_str[right]:
                        break
                    # print('{}---{}'.format(left,right))
                    if left==right or left+1 == right:
                        # print('====找到一个值为：{}===='.format(child_str))
                        return child_str
                    left+=1
                    left1+=1
                    right-=1
                    right1-=1