import numpy as np

def indexer(n):
    arr = np.empty((n, n, 2), dtype='int32')
    arr[:, :, 0] = np.arange(n)[:, None]
    arr[:, :, 1] = np.arange(n)[None, :]

    diag = [[] for _ in range(2 * n - 1)]
    for i in range(n - 1):
        diag[i] = [arr[i - j, j] for j in range(i + 1)]
    diag[n - 1] = [arr[n - 1 - j, j] for j in range(n)]

    for i in range(n - 1):
        diag[n + i] = [arr[n - 1 - j, 1 + i + j] for j in range(n - i - 1)]

    return diag

def find_outermost_pts_in_rot45(arr):
    rows, cols = arr.shape
    assert rows == cols, 'Square arrays only for now'

    n = rows
    diag = indexer(n)

    diag_bb = {}
    for id, d in enumerate(diag):
        # for el in arr[tuple(np.asarray(d).T)]:
        for ix, iy in d:
            el = arr[ix, iy]
            if not el in diag_bb:
                diag_bb[el]= [[ix,iy]]*4
            else:
                diag_bb[el][1] = [ix, iy]
                if iy - ix > diag_bb[el][2][1] - diag_bb[el][2][0]:
                    diag_bb[el][2] = [ix, iy]
                if iy - ix < diag_bb[el][3][1] - diag_bb[el][3][0]:
                    diag_bb[el][3] = [ix, iy]

    return diag_bb


if __name__ == '__main__':
    pass