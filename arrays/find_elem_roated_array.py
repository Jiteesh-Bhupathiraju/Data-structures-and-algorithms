# as thought we gonna split the array into two and then do different bs

# learned and thought: will check if the point we are the range is sorted and falls in that range esle will remove to the other side
# as the rotated is alreayd sorted means the left is always shud be grater

def rot_search(nums, target):
    if not nums: return -1

    lenn = len(nums)
    left =0
    right = lenn-1

    while left<= right:
        mid = (left + right) // 2

        if nums[mid]==target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target <=nums[mid]:
                right = mid-1 # as we already checked the mid one
            else:
                left = mid+1

        else:
            if nums[mid]<= target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
    return -1

print(rot_search([5,1,2,3,4],1))