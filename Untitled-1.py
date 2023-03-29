def hasZeroSumSublist(nums):
 
    s = set()
 
    s.add(0)
 
    total = 0
 
    for i in nums:
 
        total += i
 
        if total in s:
            return True
 
        s.add(total)
 
    return False
 