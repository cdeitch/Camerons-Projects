x = []
k = int(input("Enter size of array\n"))
print("Enter elements for array")
for i in range(0, k):
    num = int(input())
    x.append(num)


def SelectionSort(a):
    A = a.copy()
    for i in range(len(A)):
        maxIndex = i
        for j in range(i + 1, len(A)):
            if A[maxIndex] < A[j]:
                maxIndex = j

        A[i], A[maxIndex] = A[maxIndex], A[i]
    print("Unsorted array")
    for i in range(len(a)):
        print(a[i], end=" ")
    print("\nSorted array")
    for i in range(len(A)):
        print(A[i], end=" ")


SelectionSort(x)
