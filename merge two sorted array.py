def mergeArrays(arr1, arr2):
    s1 = len(arr1)
    s2= len(arr2)
    # DEclaring arr of size s1+s2
    arr3 = [0] * (s1 + s2)
    i = 0
    j = 0
    k = 0
    # merge sort
    while i < s1 and j < s2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < s1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1
    while j < s2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    print("Final list:",*arr3)
    n = s1+s2
    if n%2==1:
        print(arr3[n//2],'is the median.')
    else:
        print(arr3[n//2-1],'and',arr3[n//2],'are median.')

arr1 = list(map(int, input('Enter First List:').split()))
arr2 = list(map(int, input('Enter Second List:').split()))
mergeArrays(arr1, arr2);
