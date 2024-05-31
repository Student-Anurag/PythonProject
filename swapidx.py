n = int(input("Enter size of list: "))
list = []
for _ in range(n):
    num = int(input())
    list.append(num)
idx1 = int(input("Enter index 1: "))
idx2 = int(input("Enter index 2: "))
print(list)
tmp=list[idx1]
list[idx1] = list[idx2]
list[idx2] = tmp
print(list)
