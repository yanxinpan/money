class SparseMatrix:
    def __init__(self):
        self.coordinates = []  # the coordinates of non-zero elements
        self.values = []  # the value of non-zero elements
        self.n_rows = 0
        self.n_cols = 0

    @property
    def shape(self):
        return self.n_rows, self.n_cols

    def from_elements(self, coordinates, values, n_rows, n_cols):
        self.coordinates = coordinates
        self.values = values
        self.n_rows = n_rows
        self.n_cols = n_cols
        return self

    def from_dense_matrix(self, x):
        n, m = len(x), len(x[0])
        # Save the coordinates and values of non-zero elements
        coordinates = []
        values = []
        for i in range(n):
            for j in range(m):
                if x[i][j] != 0:
                    coordinates.append((i, j))
                    values.append(x[i][j])
        self.from_elements(coordinates, values, n, m)
        return self

    def dot(self, y):
        # convert y into a
        if not isinstance(y, SparseMatrix):
            y = SparseMatrix.from_dense_matrix(y)

        # Use two pointers to find the coordinate calculate the dot products.
        x_idx = 0
        y_idx = 0
        res = 0

        while x_idx < len(self.coordinates) and y_idx < len(y.coordinates):
            xi, xj = self.coordinates[x_idx]
            yi, yj = y.coordinates[y_idx]
            if xi > yi:
                y_idx += 1
            elif xi < yi:
                x_idx += 1
            else:
                if xj > yj:
                    y_idx += 1
                elif xj < yj:
                    x_idx += 1
                else:
                    res += self.values[x_idx] * y.values[y_idx]
        return res

