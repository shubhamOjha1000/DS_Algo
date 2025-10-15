class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:

        def prefix_sum_Array(nums) :
            PSA = []
            TS = 0
            for i in range(0, len(nums)):
                TS += nums[i]
                PSA.append(TS)
            return PSA

        

        PSA = prefix_sum_Array(nums)
        dic = {}
        TS = 0
        
        for i in range(0, len(nums)):
            if PSA[i] == k:
                TS += 1

        i = len(nums) - 1
        while i >= 0:
            if PSA[i] in dic:
                TS += 1
            
            dic[PSA[i] - k] = True
            
            i -= 1
        
        
        return TS




    
    

        """
        Naive solution

        TS = 0
        A = nums

        for i in range(0, len(A)):
            for j in range(i+1, len(A) + 1):
                NA = A[i : j]
                if sum(NA) == k:
                    TS += 1
                else:
                    continue
        
        return TS

        """