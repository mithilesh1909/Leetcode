class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x = 0
        for n in nums:
            q, r = divmod(n, k)
            if not r:
                i = q - 1
                if i >= 0:
                    x |= 1 << i

        return ((x + 1) & ~x).bit_length() * k