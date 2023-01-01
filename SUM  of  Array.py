nlist=[]
n=int(input("Please enter the number of elements in the list : "))
for i in range(1,n+1):
  value=int(input("Please enter the value of %d element : "%i))
  nlist.append(value)
  
total=sum(nlist)
print("The sum of elements in the array ",total)
