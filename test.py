class Solution:
    def myAtoi(self, strs):
        front = 1 # 前导数据判断
        res_str = '+0'
        for char in strs:
            print('当前字符:***{}***'.format(char))
            # 前导空格去除
            if char ==' ' and front:
                print('空格跳过')
                continue

            # 数据正负
            if char in ['+','-'] and front:
                front = 0
                print('获取到正负号')
                res_str = char+'0'
                continue

            if char not in list('0123456789') and front:
                return 0
            elif char not in list('0123456789'):
                print('找的不是数字，终止了')
                return int(res_str)
                break
            else:
                front = 0
                res_str+=char

            if int(res_str)<-2147483648:
                print('当前数据小于范围数据，返回最小值')
                return  -2147483648
            if int(res_str)>2147483647:
                print('当前数据大于范围数据，返回最大值')
                return 2147483647

        return int(res_str)
if __name__ == '__main__':
    strs= "-91283472332"
    solution = Solution()
    res = solution.myAtoi(strs)
    print(res)

