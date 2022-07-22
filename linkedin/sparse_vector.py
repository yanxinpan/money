class SparseVector:
    def __init__(self):
        self.elements = []
        self.length = -1

    def from_dense_vector(self,x:List):
        for i,c in enumerate(x):
            if c != 0:
                self.elements.append((i,c))
        self.length = len(x)
        return self

    def dot(self,):
