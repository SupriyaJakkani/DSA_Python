list1=[3,3,5,5,7,9,2,6]
print("Unsorted List", list1)

for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val, i) # i gives the first occurance of the value from the list
    if list1[i] != list1[min_index]:
        list1[i], list1[min_index]=list1[min_index],list1[i]
        print(list1) #if we put the print inside the loop then it will print the all iterations