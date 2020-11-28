from typing import List
class Sort:
    TOTAL_SWAPS = 0
    @staticmethod
    def selectionSort(list: List[int]):
        for i in range(len(list)):
            min = i
            for j in range(i+1, len(list)):
                if list[min] > list[j]:
                    min = j
            list[i], list[min] = list[min], list[i]
            Sort.TOTAL_SWAPS += 1

    @staticmethod
    def bubbleSort(list: List[int]):
        for i in range(len(list)):
            swapped = False
            for j in range(len(list)-i-1):
                 if list[j] > list[j+1]:
                     list[j], list[j+1] = list[j+1], list[j]
                     Sort.TOTAL_SWAPS += 1
                     swapped = True
            if not swapped:
                break

    @staticmethod
    def mergeSort(list: List[int]):
        if len(list) > 1:
            left = list[:len(list)//2]
            right = list[len(list)//2:]
            Sort.mergeSort(left)
            Sort.mergeSort(right)
            i = j = k = 0
            while i < len(left) and j< len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    Sort.TOTAL_SWAPS += 1
                    i += 1
                else:
                    list[k] = right[j]
                    Sort.TOTAL_SWAPS += 1
                    j += 1
                k += 1
            while i < len(left):
                list[k] = left[i]
                Sort.TOTAL_SWAPS += 1
                i += 1
                k += 1
            while j < len(right):
                list[k] = right[j]
                Sort.TOTAL_SWAPS += 1
                j += 1
                k += 1

    @staticmethod
    def clearSwapAmount():
        Sort.TOTAL_SWAPS = 0

#######################################################################
########################  TEST  #####  BLOCK   ########################
#######################################################################

arr = [64, 34, 25, 12, 22, 11, 90]
print(arr)
Sort.mergeSort(arr)
print(arr)
print(Sort.TOTAL_SWAPS)

