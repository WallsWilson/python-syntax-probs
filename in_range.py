def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """
    for x in nums:
        if x >= lowest or x <= highest:
            return x
        print(x)

    # YOUR CODE HERE


in_range([10, 20, 30, 40, 50], 15, 30)            
