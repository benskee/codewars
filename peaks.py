def pick_peaks(arr):
    mydict = {
        'pos': [],
        'peaks': []
    }
    copy_arr = arr.copy()
    for i in range(1, (len(arr)-1)):

        j = i+1

        if copy_arr[i] > copy_arr[i-1] and copy_arr[i] > copy_arr[j]:
            mydict['pos'].append(i)
            mydict['peaks'].append(copy_arr[i])

        elif copy_arr[i] > copy_arr[i-1] and copy_arr[i] == copy_arr[j]:
            while j < len(arr)-1:
                j +=1
                if copy_arr[i] > copy_arr[j]:
                    mydict['pos'].append(i)
                    mydict['peaks'].append(copy_arr[i])
                    break
                elif copy_arr[i] < copy_arr[j]:
                    break
    return mydict


# print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]))
# print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
# print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]))
# print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]))
# print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]))
# print(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]))
# print(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]))
print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]))
# print(pick_peaks([]))
# print(pick_peaks([1, 1, 1, 1]))
