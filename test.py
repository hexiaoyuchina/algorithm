class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        res_list =['' for x in range(numRows)]
        index,flag=0,-1
        for char in s:
            res_list[index]+=char
            if flag==1:
                print('向下字符'+char)
            else:
                print('向上字符'+char)
            if index==0 or index==numRows-1: flag =- flag
            index+=flag
            
        return ('').join(res_list) 

if __name__ == '__main__':
    numRows=2
    # strs='PAYPALISHIRING'
    # strs='PAYPALISHIRING'
    strs="ABCDEF"

    solution = Solution()
    res = solution.convert(strs,numRows)
    print(res)


