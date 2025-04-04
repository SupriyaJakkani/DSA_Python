list1=[12,45,67,89,38,43]
print("Unsorterd List:",list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
             print(list1)
    print()

print("Sorted List:",list1)