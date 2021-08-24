class Solution:
    def reverse(self, x):
        '''
        -2^31 <= x <= 2^31 - 1
        动态规划
        '''
        if len(str(x))==1:
            return x

        data_str=str(x)
        op=''
        if data_str[0] in ['+','-']:
            op = data_str[0]
            data_str=data_str[1:]

        data_str_len=len(data_str)
        mid=data_str_len//2# 向下取整
        #数量为偶数
        left_str = data_str[:mid]
        mid_str = data_str[mid] if data_str_len%2!=0 else ''
        right_str = data_str[mid:]  if data_str_len%2!=0 else data_str[mid+1:] 
        left_str_reverse = self.reverse(left_str)
        right_str_reverse = self.reverse(right_str)
        return op+right_str_reverse+mid_str+left_str_reverse

if __name__ == '__main__':
    data=123
    solution = Solution()
    res = solution.reverse(data)
    print(res)


