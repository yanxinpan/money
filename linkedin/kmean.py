import numpy as np


class KMeans:
    def __init__(self):
        self._k = None
        self._centroids = None

    def fit(self, data: np.ndarray, k: int, max_iter: int = 100, min_delta: float = 0.01):

        # Randomly initialize centroids
        n = data.shape[0]
        current_centroids = data[np.random.randint(0, n, k)]

        # Initialize params.
        next_centroids = np.empty_like(current_centroids)
        delta = float('inf')
        iter_num = 0
        labels = np.empty(n)

        while delta > min_delta and iter_num < max_iter:
            iter_num += 1

            # Assign points to its closest centroids
            for i in range(n):
                dist = np.empty(k)
                for j in range(k):
                    # Calculate the l2 distance to the centroids
                    dist[j] = np.linalg.norm(data[i] - current_centroids[j])
                # Find the closest centroids
                labels[i] = np.argmin(dist)

            # Calculate the new centroids
            for j in range(k):
                cluster_data = data[np.where(labels == j)]
                if cluster_data.shape[0] == 0:
                    # When there is no sample belong to this cluster. Update the centroid with a random sample.
                    next_centroids[j] = data[np.random.randint(0, n, 1)]
                else:
                    next_centroids[j] = np.mean(cluster_data, axis=0)

            # Calculate the changes in centroids
            delta = np.linalg.norm(next_centroids - current_centroids)
            current_centroids = next_centroids

        self._centroids = next_centroids
        self._k = k

    def predict(self, x: np.ndarray):
        if self._centroids is None:
            raise ValueError('The centroids are empty. Please trained the model before use')
        if x.shape[1] != self._centroids.shape[1]:
            raise ValueError(f'the shape of input is invalid, got {x.shape}. '
                             f'The shape of centroids are {self._centroids.shape}')

        dist = np.empty(self._k)
        labels = np.empty(x.shape[0])

        for i in range(x.shape[0]):
            for j in range(self._k):
                dist[j] = np.linalg.norm(x[i] - self._centroids[j])
            labels[i] = np.argmin(dist)
        return labels

    @property
    def get_centroids(self):
        return self._centroids


def test_kmeans():
    data = np.concatenate([np.random.normal(0, 1, size=(5, 3)),
                           np.random.normal(-1, 1, size=(4, 3)),
                           np.random.normal(1, 1, size=(3, 3))])
    print('Generated a dataset consists of 11 items from 3 clusters.')
    print('Cluster 1 has 5 items from normal distribution (mu = (0,0,0), sigma is Identity matrix)')
    print('Cluster 2 has 4 items from normal distribution (mu = (-10,-10,-10), sigma is Identity matrix)')
    print('Cluster 3 has 2 items from normal distribution (mu = (10,10,10), sigma is Identity matrix)')
    model = KMeans()
    model.fit(data, k=3)
    print('The predicted results are:')
    print(model.predict(data))
    print('The centroids are:')
    print(model.get_centroids)


if __name__ == '__main__':
    test_kmeans()
