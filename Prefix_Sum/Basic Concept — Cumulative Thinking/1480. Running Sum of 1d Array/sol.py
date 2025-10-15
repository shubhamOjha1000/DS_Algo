class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        TS = 0
        TSA = []
        for i in range(0, len(nums)):
            TS += nums[i]
            TSA.append(TS)
        return TSA