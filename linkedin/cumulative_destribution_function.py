class CDF:
    def __init__(self, values):
        self.values = values

    def f(self, x):
        #  use binary search to find the idx of the smallest value that is greater than x.
        #  Assuming the idx we found is "i", then there are i elements smaller or equal to x since idx starting from 0.
        #  The cdf of x is i/(the total num of elements)
        left = 0
        right = len(self.values)

        # search space [0, len(self.values))
        while left < right:
            mid = (left + right) // 2

            if self.values[mid] > x:
                right = mid
            else:
                left = mid + 1

        return (left * 1.0)/len(self.values)


def test_cdf():
    cdf = CDF([i for i in range(1, 11)])
    for i in range(12):
        print(cdf.f(i))


if __name__ == '__main__':
    test_cdf()
