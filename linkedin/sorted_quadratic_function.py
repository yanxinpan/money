def quadratic_function(x, a, b, c):
    res = a*x*x + b*x + c
    return res

def merge_sorted_array(X, Y):
    # The input X, Y are all non-increasing.
    # use two pointers to merge them into a non-decreasing array
    res = []
    while X and Y:
        if X[-1] < Y[-1]:
            res.append(X.pop())
        else:
            res.append(Y.pop())
    return res + X[::-1] + Y[::-1]


def sorted_quadratic_array(X, a, b, c):
    # the input X is a sorted array. The expected output is the sorted array for a*x^2 + bx +c
    # The quadratic function is symmetric at x = -b/(2a).
    # When a >0, the function is a convex, decreasing when x<-b/(2a) and increasing when x > -b/(2a);
    # Otherwise the function is concave, decreasing when x>-b/(2a) and increasing when x < -b/(2a).

    # Find the smallest x that is not larger than -b/(2a) in X by binary search:
    assert a!= 0, 'the input function is not a quadratic function'
    vertex = -b/2.0/a
    left = 0
    right = len(X) - 1
    while left < right:
        mid = (left + right) // 2
        if X[mid] >= vertex:
            right = mid
        else:
            left = mid + 1
    # end condition left == right

    # Apply the quadratic function to the array
    X = [quadratic_function(x, a, b, c) for x in X]
    if a > 0:
        # X[:left] and X[len(X):left:-1] are non-increasing arrays,
        return merge_sorted_array(X[:left], X[len(X):left:-1])
    else:
        # X[left:] and X[left+1:0-1] are non-increasing arrays,
        return merge_sorted_array(X[left:], X[:left][::-1])


def test_sorted_quadratic_array():
    X = list(range(-5, 5))
    a = 1
    b = 2
    c = -1
    print(f'The original sorted array is: {X}')
    print(f'the sorted quadratic array (x^2 + 2x -1) is  {sorted_quadratic_array(X, a, b, c)}')
    a = -1
    print(f'the sorted quadratic array (-x^2 + 2x -1)is  {sorted_quadratic_array(X, a, b, c)}')


if __name__ == '__main__':
    test_sorted_quadratic_array()


