nums = list(map(int, input().split()))
n = int(input())
for i in range(1, len(nums)):
    key = nums[i]
    j = i=1
    while j>=0 and nums[j] > key:
        nums[j+1] = nums[j]
        j = j-1