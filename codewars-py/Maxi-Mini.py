def maximum(arr):
    maxi = arr[0]
    for i in arr:
        if i >= maxi:
            maxi = i
    return maxi

def minimum(arr):
    mini = arr[0]
    for i in arr:
        if i <= mini:
            mini = i
    return mini