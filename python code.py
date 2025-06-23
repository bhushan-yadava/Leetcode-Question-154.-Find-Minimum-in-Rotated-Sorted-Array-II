class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # Initialize the left and right pointers to the start and end of the list respectively
        left, right = 0, len(nums) - 1
      
        # Continue searching while the left pointer is less than the right pointer
        while left < right:
            # Find the middle index by using bitwise right shift operation (equivalent to integer division by 2)
            mid = (left + right) >> 1
          
            # If the middle element is greater than the element at the right pointer...
            if nums[mid] > nums[right]:
                # ... the smallest value must be to the right of mid, so move the left pointer to mid + 1
                left = mid + 1
            # If the middle element is less than the element at the right pointer...
            elif nums[mid] < nums[right]:
                # ... the smallest value is at mid or to the left of mid, so move the right pointer to mid
                right = mid
            # If the middle element is equal to the element at the right pointer...
            else:
                # ... we can't be sure of the smallest, but we can reduce the search space by decrementing right pointer
                right -= 1
      
        # When the left pointer equals the right pointer, we've found the minimum, so return the element at left pointer
        return nums[left]
