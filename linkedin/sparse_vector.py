import numpy as np


class SparseVector:
    def __init__(self):
        self.elements = []  # List of tuples, which are (idx, value) for all non-zero elements sorted by idx.
        self.length = -1

    def from_dense_vector(self, x):
        for i, c in enumerate(x):
            if c != 0:
                self.elements.append((i, c))
        self.length = len(x)
        return self

    def dot(self, y):
        if not isinstance(y, SparseVector):
            y = SparseVector().from_dense_vector(y)

        #  use two pointers to find and calculate the dot product
        res = 0
        i = 0
        j = 0

        while i < len(self.elements) and j < len(y.elements):
            x_idx, x_value = self.elements[i]
            y_idx, y_value = y.elements[j]
            if x_idx == y_idx:
                # when both vectors has non-zero elements at the same idx, add the product to result
                res += x_value * y_value
                # move both pointers to the next non-zero element
                i += 1
                j += 1
            elif x_idx > y_idx:
                # when the current non-zero idx in x is larger than y, move the pointer in y to the next element.
                j += 1
            else:
                # when the current non-zero idx in y is larger than x, move the pointer in x to the next element.
                i += 1

        return res


def test_sparse_vector():
    x = np.array([1, 0, 0, 3, 0, 0, 0, 5, 0])
    y = np.array([0, 0, 1, 2, 0, 0, 0, -1, -4])
    x_sparse = SparseVector().from_dense_vector(x)
    y_sparse = SparseVector().from_dense_vector(y)
    sparse_res = x_sparse.dot(y_sparse)
    np_res = x.dot(y)
    assert sparse_res == np_res
    print(f'sparse res is : {sparse_res}')
    print(f'res from numpy is: {np_res}')


if __name__ == '__main__':
    test_sparse_vector()
