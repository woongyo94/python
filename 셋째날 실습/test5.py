
list_a = [[1,2,3,4,5,6,7,8,9], 3, "false"]
print (list_a[0][3:-5])


list_b=[1,2,3,4]
list_c=[4,5,6]

print (list_b+list_c)
print (list_b*3)
print (len(list_b))

list_a.append(10)

print(list_a)
list_a.insert(0,10)
print(list_a)
list_a.insert([0][0],10)
print(list_a)
list_a.extend([12])
print(list_a)

list_a.pop(2)
del list_a[2]
print(list_a)
list_a.clear()
print(list_a)
