def BinarySearch(list1,key):
    lower=0
    upper=len(list1)-1
    Found= False
    while lower<=upper and not Found:
        mid= (lower+upper)//2
        if key== list1[mid]:
            Found= True
        elif key>list1[mid]:
            lower=mid+1
        else:
            upper=mid-1
    if Found == True:
         print("Key is Found")
    else:
         print("Key is not Found")
         
list1=[2,6,7,9,4,5,8]
list1.sort()
print(list1)
key=int(input("Enter a Key : "))
BinarySearch(list1,key)