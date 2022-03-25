import math


def rotate(nums, k):
    count = len(nums)
    k %= count
    if k != 0:
        round = math.gcd(count, k)
        for i in range(round):
            cur, buf = i, nums[i]
            while True:
                next = (cur + k) % count
                buf, nums[next] = nums[next], buf
                cur = next
                if cur == i:
                    break


def rotate_(nums, k):
    """反转数组"""
    def reverse(arr):
        """unnecessary function"""
        print('reverse before: ' + str(arr))
        arr[:] = arr[::-1]
        print('id(arr): ' + str(id(arr)))
        print('reverse  after: ' + str(arr))
    # print('id(nums): ' + str(id(nums)))

    k %= len(nums)
    # reverse(nums)
    # reverse(nums[:k])
    # reverse(nums[k:])

    print(nums)
    nums[:] = nums[::-1]

    # nums[:k] = nums[:k:-1]
    # nums[k:] = nums[k::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    print(nums)


def reverse(nums, k):
    """not work in this way"""
    print(nums)
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    nums[:] = nums[::-1]
    print(nums)


if __name__ == '__main__':
    nums_ = [1,2,3,4,5,6,7]
    # rotate(nums_, 3)
    rotate_(nums_, 3)
    # print(nums_)

    # reverse(nums_, 3)
