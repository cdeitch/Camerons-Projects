x = []
k = int(input("Enter size of array\n"))
print("Enter elements for array")
for j in range(0, k):
    num = int(input())
    x.append(num)


def TwoLargest(a, b):
    large1 = 0
    large2 = 0
    for i in range(0, b):
        if a[i] > large1:
            large2 = large1
            large1 = a[i]
        elif large2 < a[i]:
            large2 = a[i]
    return large1, large2


large_1, large_2 = TwoLargest(x, k)
print(large_1, large_2)
