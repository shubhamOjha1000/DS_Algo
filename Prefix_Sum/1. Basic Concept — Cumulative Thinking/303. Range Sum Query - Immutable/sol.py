class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        NA = self.nums[left : right + 1]
        TS = 0
        for i in range(0, len(NA)):
            TS += NA[i]
        return TS
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)