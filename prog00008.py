def get_index(l, p):
    first_index = 0
    last_index = len(l)-1
    mid = 0
    while first_index <= last_index:
        mid = (first_index+last_index) // 2
        if l[mid] == p:
            return mid
        elif p < l[mid]:
            last_index = mid - 1
        else:
            first_index = mid + 1
    return mid


l = [2, 5, 7, 18, 20]
p = 20
print(get_index(l, p))
