array = [7,5,9,0,1,2,4,3,6,8]


for i in range(len(array)):
    min = i
    for j  in range(i+1 ,len(array)):
        if array[min] > array[j]:

         min = j

    array[i] , array[min] = array[min] ,array[i]


print(array)
