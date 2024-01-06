# import random


def nums_less_value(result, nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] != nums[j] and nums[i] > nums[j]:
                count += 1
        result.append(count)
        count = 0
    return result


if __name__ == '__main__':
    result = []
    # nums = [random.randrange(1, 100) for i in range(0, 10)]
    nums = input().split()
    nums = list(map(int, nums))
    print(
        ' '.join(
            str(i) for i in nums_less_value(result, nums)
        )
    )
