n = int(input("Enter the number of elements:"))
nums = list(map(int, input().split()))
if n == len(nums):
    for i in range(n):
        for j in range(n):
            if (nums[i] > nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)
else:
    print("numbers length isn't matching dude")
