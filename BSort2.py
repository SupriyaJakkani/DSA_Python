list1=[]
num=int(input("How many numbers you want to enter:"))
print("Enter the values:")
for k in range(num):
    list1.append(int(input()))
print("Unsorted List:",list1)

for j in range(len(list1)-1):
        for i in range(j):
                 if list1[i]>list1[i+1]:
                     list1[i],list1[i+1]=list1[i+1],list1[i]
                     print(list1)

print("Sorted List:",list1)
                 
                 