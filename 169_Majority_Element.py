# space O(n)
# time O(n)
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common()[0][0]