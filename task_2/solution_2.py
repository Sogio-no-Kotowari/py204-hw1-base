a=input()
max=0
for element in a:
  
  k=0  
  for symbol in a:
    if element==symbol:
          k=k+1
        
    if k>=max:
        max=k
        g=element  
print ("самый частый элемент - ", g)
 
