import math
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
    p_positive = 0

    if nums[0] >= 0:
        return [n*n for n in nums]
    elif nums[-1] < 0:
        ans = [n*n for n in nums]
        ans.reverse()
        return ans
    else:
        for n in nums:
            if n < 0:
                p_positive += 1
            else:
                break
        p_negative = p_positive-1
        ans = []
        count = len(nums)
        while p_negative >= 0 and p_positive < count:
            s_positive = int(math.pow(nums[p_positive], 2))
            s_negative = int(math.pow(nums[p_negative], 2))
            # ans.append(s_positive if s_positive > s_negative else s_negative)
            if s_positive > s_negative:
                ans.append(s_negative)
                p_negative -= 1
            else:
                ans.append(s_positive)
                p_positive += 1

        while p_negative >= 0:
            ans.append(int(math.pow(nums[p_negative], 2)))
            p_negative -= 1

        while p_positive < count:
            ans.append(int(math.pow(nums[p_positive], 2)))
            p_positive += 1

        return ans


if __name__ == '__main__':
    # nums = [-4,-1,0,3,10]
    nums = [-10000,-9999,-7,-5,0,0,10000]
    print(sortedSquares(nums))



