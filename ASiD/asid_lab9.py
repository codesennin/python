from typing import List, Any
class Sort:
    @staticmethod
    def bubbleSort(list: List[Any], reversed = False):
        swapped = False     # dzięki temu pętla nie kręci się niepotrzebnie gdy już wszystko jest posortowane
        for x in range(len(list)):
            for y in range(len(list)-x-1):
                if reversed:
                    if list[y] < list[y + 1]:
                        list[y], list[y + 1] = list[y + 1], list[y]
                        swapped = True
                else:
                    if list[y] > list[y+1]:
                        list[y], list[y+1] = list[y+1], list[y]
                        swapped = True
            if not swapped:
                break

    @staticmethod
    def selectionSort(list: List[Any], reversed = False):
        for x in range(len(list)):
            min = x
            for j in range(x+1, len(list)):
                if reversed:
                    if list[min] < list[j]:
                        min = j
                else:
                    if list[min] > list[j]:
                        min = j
            list[x], list[min] = list[min], list[x]

    @staticmethod
    def insertionSort(list: List[Any], reversed = False):
        for x in range(1, len(list)):
            key = list[x]
            y = x-1
            if reversed:
                while y >= 0 and key > list[y]:
                    list[y+1] = list[y]
                    y -= 1
            else:
                while y >= 0 and key < list[y]:
                    list[y+1] = list[y]
                    y -= 1
            list[y+1] = key

l1 = [6, 1, 7, 3, 4, 9, 2, 5, 8, 0]
l2 = [8, 5, 4, 2, 1, 7, 9, 6, 0, 3]
l3 = [3, 4, 0, 7, 1, 5, 2, 8, 9, 6]
l4 = [3, 4, 1, 2, 5, 0, 9, 8, 6, 7]
l5 = [3, 5, 8, 7, 1, 6, 9, 4, 0, 2]
l6 = [0, 7, 9, 4, 8, 6, 5, 3, 2, 1]
l7 = [9, 2, 1, 5, 8, 0, 6, 4, 3, 7]
l8 = [4, 5, 2, 7, 0, 9, 1, 3, 6, 8]
l9 = [0, 8, 2, 7, 6, 3, 9, 1, 5, 4]
l10 = [2, 0, 7, 3, 4, 5, 8, 6, 9, 1]

Sort.bubbleSort(l1)
Sort.bubbleSort(l2, True)
Sort.bubbleSort(l3)
Sort.selectionSort(l4)
Sort.selectionSort(l5)
Sort.selectionSort(l6, True)
Sort.insertionSort(l7)
Sort.insertionSort(l8)
Sort.insertionSort(l9, True)
Sort.bubbleSort(l10)

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
print(l8)
print(l9)
print(l10)