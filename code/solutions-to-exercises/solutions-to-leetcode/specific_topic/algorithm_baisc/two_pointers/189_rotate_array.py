import math


def rotate(nums, k):
    count = len(nums)
    k %= count
    if k != 0:
        round = math.gcd(count, k)
        for i in range(round):
            cur, buf = i, nums[i]
            start = cur
            while True:
                next = (cur + k) % count
                buf, nums[next] = nums[next], buf
                cur = next
                if cur == i:
                    break



if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    rotate(nums, 3)
    print(nums)
