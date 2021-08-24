class Solution:
    def process(self,x):
        
        data_str=str(x)
        op=''
        if data_str[0] in ['+','-']:
            op = data_str[0]
            data_str=data_str[1:]
        if len(str(data_str))==1:
            return x
        data_str_len=len(data_str)
        mid=data_str_len//2# 向下取整
        
        #数量为偶数
        left_str = data_str[:mid]
        mid_str = data_str[mid] if data_str_len%2!=0 else ''
        right_str = data_str[mid+1 :]  if data_str_len%2!=0 else data_str[mid:] 
        print('当前字符串：{}，长度：{}，中值：{}，左侧值：{}，右侧值：{}'.format(data_str,data_str_len,mid,left_str,right_str))
        left_str_reverse = self.process(left_str)
        right_str_reverse = self.process(right_str)
        return op+right_str_reverse+mid_str+left_str_reverse
        
    def reverse(self, x):
        '''
        -2^31 <= x <= 2^31 - 1
        动态规划
        '''
        
        res = int(self.process(x))
        top=2**31
        if res<-top or res>top-1:
            return 0
        else:
            return res
        
        
        

        return res

if __name__ == '__main__':
    data=-1
    solution = Solution()
    res = solution.reverse(data)
    print(res)


