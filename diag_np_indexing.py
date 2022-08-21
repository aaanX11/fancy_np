import numpy as np

def diag_index(img):
    n = 320
    arr = np.arange(n ** 2).reshape((n, n))
    diag = [[] for _ in range(2 * n - 1)]
    for i in range(n - 1):
        diag[i] = [arr[i - j, j] for j in range(i + 1)]
    diag[n - 1] = [arr[n - 1 - j, j] for j in range(n)]

    for i in range(n - 1):
        diag[n + i] = [arr[n - 1 - j, 1 + i + j] for j in range(n - i - 1)]

    rows, cols = img.shape

    for id, d in enumerate(diag):
        t = img.ravel()[d]
        for idx, el in enumerate(img.ravel()[d]):
            print(el)
        print()


if __name__ == '__main__':
    pass