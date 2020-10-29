a=input("введите последовательность")
max=0
for element in a:
    my_int_element= int(element)
    if my_int_element>=max:
        max=my_int_element

print ("max=",max)
