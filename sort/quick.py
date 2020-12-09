def partition(a, m, n):
    key = a[n-1]

    i = m
    for j in range (m, n - 1):
        if a[j] < key:
            a[i], a[j] = a[j], a[i]
            i+=1
        
    a[i],a[n-1] = a[n-1],a[i]

    return i


def qsort(a, m, n):
    if m < n:
        q = partition (a, m, n)
        qsort(a, m, q)
        qsort(a, q+1, n)


def quick_sort (a):
    qsort(a, 0, len(a))

    return a