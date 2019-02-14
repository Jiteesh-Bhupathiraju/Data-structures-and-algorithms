# have two pointers and move in accordance to comparision and then pop when met the kth
# the whole idea is to eliminate k/2 elements rather /2 of the given arrays of larger lengthgs

def kth_two_sorted_arays(a,b,la,lb,k):

    if la > lb:
        return kth_two_sorted_arays(b,a,lb,la,k)

    if la ==0:
        return b[k-1]

    if k==1:
        return min(a[0], b[0])

    i=min(la,k//2)
    j = min(lb, k//2)

    if a[i-1] < b[j-1]:
        return kth_two_sorted_arays(a[i:], b, la-i, j, k-i)
    else:
        return kth_two_sorted_arays(a,b[j:], i, lb-j, k-j)