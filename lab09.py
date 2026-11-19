# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # find 2 index positions that add up to the target
    #e.g = [3,2,4], target = 6
    #at check pairs: 3+2 - 5 (no), 3+4 = 7 (no), 2+4 = 6 (yes)
    #loop thrgouh nums once, store each numberr & index in a dictionary
    # and check if (target-num) was already stored from previous index
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i


def max_profit(prices):
    # Outline:
    #picka a day to buy and a later day to sell for the max profit (0 if prices only drop )
    #  example : [7,1,5,3,6,4]
    #if i buy at 7, I lose money everywhere. If i buy at 1 which is day 1 and sell at 6 which is day 4,
    #profit is 6-1 = 5.
    #can't sell before buying, so as i go left to right, just keep track of the
    #cheapest price ive passed so far, and check if selling today beats my best profit.
    #approach : loop through the prices once form the left to right. keep track of the 
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        elif price - min_price > best_profit:
            best_profit = price - min_price

    return best_profit




def max_subarray(nums):
    # Outline:
    #find the largest total from a contiguous slice of numbers in nums
    #exmaple: nums = [-2,1,-3,4,-1,2,1] -> -2 and -3 drag the sum down, so
    #starting at 4 and taking [4,-1,2,1] gives 6
    #approach: walk through the list keeping a current_sum and a best_sum. at each
    #number, decide whether to add it to current_sum or start fresh at that number
    # (whichever is larger), then update best_sum if current_sum is higher.
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    current_sum = nums[0]
    best_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum    


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass      


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
