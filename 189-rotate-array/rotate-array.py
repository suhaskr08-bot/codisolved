class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        rotation=k%len(nums)
        nums[:] = nums[-rotation:] + nums[:-rotation]