array1 = [45, 89, 10, 23, 67]

array2=[]

import random
def random_num(num1):
    for x in range(0, num1):
        num=random.randrange(0, 10000)
        array2.append(num)

def bubbleSort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)-1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    print array

random_num()
bubbleSort(array2)
