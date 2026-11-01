import requests
def arr():
    nums = [2, 4, 6, 8]
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)
    print(nums)
def a():
    nums = [2, 4, 6, 8]
    for n in nums:
        if n % 2 != 0:
            print(n)
a()
