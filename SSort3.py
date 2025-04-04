#Selection Sort----Not using "min" method
list1=[3,5,6,7,2,8,9,4,1]
print("Unsoerted List: ", list1)

for i in range(len(list1)-1):
    min_val=list1[i]
    for j in range(i+1, len(list1)):
        if list1[j]<min_val:
            min_val=list1[j]
            
    min_index=list1.index(min_val,i)
    if list1[i]!= list1[min_index]:
         list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)