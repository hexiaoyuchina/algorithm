class Solution:
    def maxArea(self, height):
        """
        双指针的方法

        移动小不移动大的原因（双指针能排除多个的原因）：
            从边界开始。

            小的决定水面高度，无论怎么移动大的，
            水面高度要么不变要么变小，单两柱子间的距离变小，
            所以移动大的要么不变要么变小，所以大的移动的意义不大，可以排除其他的。
            例如：0高度最小，7的是大的
            由于 7 号柱子已经是离 0 号柱子最远的了，水的宽度也最大，
            如果换其他的柱子和 0 号柱子配对，水的宽度只会更小，高度也不会增加，容纳水的面积只会更小，一下子排除其他
            6....1的柱子直接排除

        """

        right = len(height)-1
        left = 0
        max_area = 0
        while left<right:
            current_area = (right-left)*min(height[left],height[right])
            if current_area > max_area:
                max_area = current_area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
        
if __name__ == '__main__':
    height = [4,3,2,1,4]
    solution = Solution()
    res = solution.maxArea(height)
    print(res)











