list1 = [] 
  
while True:
  print("Enter number")  
  num=input()
  if(num=="done"):
    break
  else:
    num=int(num)
    list1.append(num)  
    
print("Largest number is:", max(list1))
