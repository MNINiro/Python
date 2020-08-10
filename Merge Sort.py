def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    right, left = [], []

    for i in range(n1):
        left.append(arr[p + i])

    for j in range(n2):
        right.append(arr[q + j + 1])

    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


if __name__ == '__main__':
    test = [5, 2, 4, 7, 1, 3, 2, 6]
    merge_sort(test, 0, len(test) - 1)
    print (test)
