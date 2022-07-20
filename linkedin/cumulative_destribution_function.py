class CDF:
    def __init__(self, values):
        self.values = values

    def f(self, x):
        #  use binary search to find the largest value that is not greater than x
        left = 0
        right = len(self.values)

        while left + 1 < right:
            mid = (left + right) // 2

            if self.values[mid] > x:
                right = mid - 1
            else:
                left = mid

        if left == 0 and self.values[left] > x:
            return 0
        if right != len(self.values) and self.values[right] <= x:
            return (right + 1.0) / len(self.values)

        return (left + 1.0)/len(self.values)


def test_cdf():
    cdf = CDF([i for i in range(1, 11)])
    for i in range(12):
        print(cdf.f(i))


if __name__ == '__main__':
    test_cdf()