#Robber
def rob(nums):
    def simple_robs(nums):
        prev,curr = 0,0
        for num in nums:
            prev,curr = curr,max (prev + num,curr)
        return curr
    
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums [0]
    else:
        return max(simple_rob(nums[1:]),simple_rob(nums[:1]))