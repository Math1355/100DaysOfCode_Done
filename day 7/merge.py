
def merge(nums1, nums2):
    m = []
    n = []
    matriz = []

    for num in nums1:
        if num > 0:
            m.append(num)

    for num in nums2:
        if num > 0:
            n.append(num)

    if (len(nums1) == len(m) + len(n)) and (len(nums2) == len(n)):
        for num in m:
            matriz.append(num)
        for num in n:
            matriz.append(num)
        matriz.sort()
        return matriz
    else:
        return "Unable to merge!"

if(__name__ == "__main__"):
    merge()