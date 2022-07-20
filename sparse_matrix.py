class SparseMatrix:
    def __init__(self):
        self.elements = []
        # .elements are list of dictionary.
        # elements[i] is the dictionary of non-zeros elements in i-th row in the matrix.
        # The key is the col idx of the non-zeros elements and the value is the element value.
        self.n_rows = 0
        self.n_cols = 0

    @property
    def shape(self):
        return self.n_rows, self.n_cols

    def from_elements(self, elements, n_rows, n_cols):
        self.elements = elements
        self.n_rows = n_rows
        self.n_cols = n_cols
        return self

    def from_dense_matrix(self, x):
        n, m = len(x), len(x[0])
        # Save the coordinates and values of non-zero elements
        elements = []
        for i in range(n):
            cur_row = {}
            for j in range(m):
                if x[i][j] != 0:
                    cur_row[j] = x[i][j]
            elements.append(cur_row)
        self.from_elements(elements, n, m)
        return self

    def dot(self, y):
        # convert y into a SparseMatrix Object
        if not isinstance(y, SparseMatrix):
            y = SparseMatrix().from_dense_matrix(y)

        # Check matrix shape
        if self.n_cols != y.n_rows:
            raise ValueError(f'The shape of matrix do not match, got {self.shape} and {y.shape}')

        # Initialize the matrix of results
        element_list = []

        for i in range(self.n_rows):
            element_dict = {}
            for j in range(y.n_cols):
                element = 0
                for k, v in self.elements[i].items():
                    if y.elements[k].get(j):
                        element += v * y.elements[k].get(j)
                element_dict[j] = element
            element_list.append(element_dict)
        return SparseMatrix().from_elements(element_list, self.n_rows, y.n_cols)


def test_sparse_matrix():
    x = [[1, 0, 0], [-1, 0, 3]]
    y = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(f'The first matrix is: {x}')
    print(f'The second matrix is: {y}')
    x = SparseMatrix().from_dense_matrix(x)
    print(f'There dot product is {x.dot(y).elements}')


if __name__ == '__main__':
    test_sparse_matrix()
