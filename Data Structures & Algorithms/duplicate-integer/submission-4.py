class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      hs=set()
      for num in nums :
        if num in hs:
            return True
        else:
            hs.add(num)
      return False