class Solution(object):
    
    def get(self,nums1,nums2,mid):
        mid_2=mid//2
        a_index=mid_2-1
        b_index=mid_2-1

        if mid_2==1:
            if nums1[a_index] <=nums2[b_index]:
                return nums1[a_index]
            elif nums1[a_index] >nums2[b_index]:
                return nums2[b_index] 
        else:
            if nums1[a_index] <=nums2[b_index]:
                res=self.get(nums1[a_index+1:],nums2,mid-a_index+1)
            elif nums1[a_index] >nums2[b_index]:
                res=self.get(nums1,nums2[b_index+1:],mid-b_index+1)
        return res

    def findMedianSortedArrays(self, nums1, nums2):
        nums1_len=len(nums1)
        nums2_len=len(nums2)
        mid=(nums1_len+nums2_len)//2
        res=self.get(nums1,nums2,mid)
        

        

if __name__ == '__main__':
    Solution=Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    res=Solution.findMedianSortedArrays(nums1,nums2)
    print(res)

            


# def get(self,nums1,nums2,mid):
#         mid_2=mid//2
#         a_index=min(nums1_len-1,mid_2)
#         b_index=min(nums2_len-1,mid_2)
#         if mid_2==1:
#             if nums1[a_index] <=nums2[b_index] and nums1_len!=0 and nums2_len!=0 or nums2_len==0:
#                 return nums1[a_index]
#             elif nums1[a_index] >=nums2[b_index] and nums1_len!=0 and nums2_len!=0 or nums1_len==0:
#                 return nums2[b_index] 
#         else:
#             if nums1[a_index] <=nums2[b_index] and nums1_len!=0 and nums2_len!=0 or nums2_len==0:
#                 res=self.get(nums1[a_index:],nums2,mid-a_index)
#             elif nums1[a_index] >=nums2[b_index] and nums1_len!=0 and nums2_len!=0 or nums1_len==0:
#                 res=self.get(nums1,nums2[b_index:],mid-b_index)
#         return res

#     def findMedianSortedArrays(self, nums1, nums2):
#         nums1_len=len(nums1)
#         nums2_len=len(nums2)
#         mid=(nums1_len+nums2_len)//2
#         res=self.get(nums1,nums2,mid)