class Solution(object):
    def get_min(self,data1,data2):
        if data1< data2:
            return data1
        else:
            return data2

    def get(self,nums1,nums2,mid):
        # 对于长度为0的列表处理
        mid_2=mid//2
        a_index=min(mid_2-1,len(nums1)-1)
        b_index=min(mid_2-1,len(nums2)-1)
        print('nums1:mid_2:{}--a_index:{}--nums1_len{}'.format(mid_2,a_index,len(nums1)))
        print('nums2:mid_2:{}--b_index:{}--nums2_len{}'.format(mid_2,b_index,len(nums2)))

        if len(nums1)==0:
            return nums2[mid-1]

        if len(nums2)==0:
            return nums1[mid-1]

        if mid==1:
            return self.get_min(nums1[0],nums2[0])
        
        if nums1[a_index] <=nums2[b_index]:
            return self.get(nums1[a_index+1:],nums2,mid-(a_index+1))
        elif nums1[a_index] >nums2[b_index]:
            return self.get(nums1,nums2[b_index+1:],mid-(b_index+1))

    def findMedianSortedArrays(self, nums1, nums2):
        nums1_len=len(nums1)
        nums2_len=len(nums2)
        mid=(nums1_len+nums2_len)//2
        right =  self.get(nums1,nums2,mid+1)
        print('right：{}'.format(right))
        if (nums1_len+nums2_len)%2==0:
            left =self.get(nums1,nums2,mid)
            print('left：{}'.format(left))
            res=(left+right)/2
        else:
            res=right
        return res
        

        

if __name__ == '__main__':
    Solution=Solution()
    #2 2.5 0 1 2
    # nums1,nums2=[1,3],[2]
    # nums1,nums2=[1,2],[3,4]
    # nums1,nums2=[0,0],[0,0]
    # nums1,nums2=[],[1]
    # nums1,nums2=[2],[]
    nums1,nums2=[1],[2,3,4,5,6]
    # nums1,nums2 =[4],[1,2,3,5,6]

    res=Solution.findMedianSortedArrays(nums1,nums2)
    print(res)