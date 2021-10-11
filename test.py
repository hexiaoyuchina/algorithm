class Solution:
    def isMatch(self, s, p):
        """
            动态规划，从下向上
            创建数组记录数据值是否匹配,用于动态规划
        """
        strs_len = len(s)
        pattern_len = len(p)
        
        # 初始化数组 0 0 ，字符串为空时
        dp = [[False]*(pattern_len+1)  for i in range(strs_len+1) ]
        # 对数组进行初始化
        dp[0][0] = True # 空串进行匹配成功
        
        # 数组第一列进行初始化：匹配串为空串,字符串每个子串匹配都会匹配不上
        for i in range(1,strs_len+1):
            dp[i][0]=False

        # 数组第一行进行初始化：字符串为空串，字符或者.指定匹配不上，指定为False,空字符串匹配空字符串为True
        for j in range(1,pattern_len+1):
            dp[0][j]=dp[0][j-2] if p[j-1]=='*' else False # 字符串为空串，遇到匹配串为*，忽略字符串与※的组合，直接依据前面的匹配串子串匹配结果，是什么就是什么
       
        for i in range(1,strs_len+1):
            s_char = s[i-1]
            for j in range(1,pattern_len+1):
                p_char = p[j-1]
                if p_char=='*':#匹配串的当前字符为*
                    # *号前的字符与字符串当前字符相等或者*号前的为万能符.
                    if dp[i][j-2]:# 为True表示：字符和*的组合中的字符即使匹配0次，之前的也匹配
                            dp[i][j] = dp[i][j-2]
                    elif p[j-2]==s_char or p[j-2]=='.':# 为Fasle：表示若字符和*的组合中的字符匹配0次则不匹配，可能匹配了1次或者多次，之前匹配就匹配不匹配就匹配
                        dp[i][j] = dp[i-1][j]   # 相等的话，前面的字符出现多次，之前匹配的话再添加个该字符也会匹配，不匹配的话再加一个字符也不会匹配
                elif s_char==p_char or p_char=='.': # 字符串或者. 
                    # print(dp[i-1][j-1])
                    # print('{}-------{}'.format(i-1,j-1))
                    dp[i][j]=dp[i-1][j-1] # 当前匹配串p-c为字符，p-0.......p-c-1  与 s-0........s-r-1的匹配结果是什么就是什么    
        print(dp) 
        return dp[strs_len][pattern_len]

if __name__ == '__main__':
    # strs = 'aaa'
    # pattern='a*a'
    strs = "ab"
    pattern = ".*c"
    # strs = "mississippi"
    # pattern="mis*is*p*."
    solution = Solution()
    res = solution.isMatch(strs,pattern)
    print(res)



