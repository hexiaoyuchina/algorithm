class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        data_str = str(x)
        data_str_len = len(data_str)
        if data_str_len==1:
            print('--')
            return True
        if data_str_len==2:
            if data_str[0]==data_str[1]:
                rint('--')
                return True
            else:
                return False

        left_start = 0
        right_end= data_str_len-1
        mid = data_str_len//2
        if data_str_len%2 ==0:
            left_end = mid
            right_start = mid+1
        else:
            left_end = mid-1
            right_start = mid+1

        print('left_start：{}，left_end：{}，right_start：{}, right_end：{}'.format(left_start,left_end,right_start,right_end))
        while left_start<=left_end:
            if data_str[left_start] == data_str[right_end] and data_str[left_end] == data_str[right_start]:
                if left_start == left_end:
                    return True
                left_start+=1
                left_end-=1
                right_start+=1
                right_end-=1
            else:
                return False
        print(left_end,left_start)
        if left_end+1 == left_start:
            return True
        

        

if __name__ == '__main__':
    data=1001
    solution = Solution()
    res = solution.isPalindrome(data)
    print(res)

