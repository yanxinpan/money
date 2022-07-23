from collections import deque


class MovingAverage:
    def __init__(self, size):
        self.q = deque([])
        self.size = size
        self.moving_average = 0.0

    def get_next_average(self, x):
        if len(self.q) < self.size:
            self.q.append(x)
            self.moving_average = 1.0 * (self.moving_average * len(self.q - 1) + x) / len(self.q)
        else:
            head = self.q.popleft()
            self.moving_average = self.moving_average - 1.0 * (head + x) / self.size
            self.q.append(x)
        return self.moving_average


class MovingAverageVariance(MovingAverage):
    def __init__(self, size):
        super.__init__(size)
        self.moving_variance = 0.0

    def get_next_variance(self, x):
        old_moving_average = self.moving_average
        old_moving_variance = self.monving_variance

        if len(self.q) < self.size:
            new_moving_average = self.get_next_average(x)
            new_moving_variance = (old_moving_variance * (len(self.q) - 1) + x ** 2
                                   + old_moving_average ** 2 * (len(self.q) - 1)
                                   - new_moving_average ** 2 * len(self.q)
                                   ) / len(self.q)
        else:
            head = self.q[0]
            new_moving_average = self.get_next_average(x)
            new_moving_variance = old_moving_variance - head ** 2 / self.size + x ** 2 / self.size \
                                  + old_moving_average ** 2 - new_moving_average ** 2
        self.moving_variance = new_moving_variance
        return self.moving_variance


def test_moving_average_and_variance():
    m_ave_var = MovingAverageVariance(4)
    for x in range(7):
        print(x)
        print(m_ave_var.get_next_variance(x))


if __name__ == '__main__':
    test_moving_average_and_variance()
