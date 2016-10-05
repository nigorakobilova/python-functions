
arr = [56, 89, 23, 45, 12, 90, -1]

def selectionSort(array):
    for j in range(len(array)-1):
        minimum = arr[j]
        for i in range(j+1, len(array)):
            if arr[i] < minimum:
                minimum = arr[i]
                index = i
        if arr[index] < arr[j]:
            temp = arr[j]
            arr[j] = minimum
            arr[index] =  temp
        elif arr[index] >= arr[j]:
            continue
    print array

selectionSort(arr)
