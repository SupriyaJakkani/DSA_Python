list1=[2,7,9,45,22,41]
print(list1)
for i in range(len(list1)):
    min_val=min(list1[i:]) #to find minimum value in every iteration and to descending order only we use "max" in "min" place
    min_index=list1.index(min_val) #for find the index  of minimum value
    list1[i],list1[min_index]=list1[min_index],list1[i] # to swap the minimum value

print(list1)