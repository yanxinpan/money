from collections import deque
import numpy as np


class MovingAverageVariance:
    def __init__(self, size):
        self.q = deque([])
        self.size = size
        self.moving_average = 0.0
        self.moving_variance = 0.0

    def next(self, x):
        old_moving_average = self.moving_average
        old_moving_variance = self.moving_variance

        if len(self.q) < self.size:
            self.q.append(x)
            new_moving_average = 1.0 * (self.moving_average * (len(self.q) - 1) + x) / len(self.q)
            new_moving_variance = (old_moving_variance * (len(self.q) - 1) + x ** 2
                                   + old_moving_average ** 2 * (len(self.q) - 1)
                                   - new_moving_average ** 2 * len(self.q)
                                   ) / len(self.q)
        else:
            head = self.q.popleft()
            new_moving_average = self.moving_average + 1.0 * (x - head) / self.size
            new_moving_variance = old_moving_variance - head ** 2 / self.size + x ** 2 / self.size \
                                  + old_moving_average ** 2 - new_moving_average ** 2
            self.q.append(x)

        self.moving_average = new_moving_average
        self.moving_variance = new_moving_variance
        return self.moving_average, self.moving_variance


def test_moving_average_and_variance():
    m_ave_var = MovingAverageVariance(4)
    for x in range(7):
        print(x)
        res = m_ave_var.next(x)
        print(m_ave_var.q)
        print(f'moving average is {res[0]} and variance is {res[1]}')
        print(np.mean(m_ave_var.q))
        print(np.var(m_ave_var.q))


if __name__ == '__main__':
    test_moving_average_and_variance()
