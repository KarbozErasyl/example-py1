# dynamic array
number = [5,8,7,4,6,9,3,2,1]
print(number[0])
print(number[1])
print(number[2])
print(number[3])
print(number[4])
number[2] = 10
print(number[2])
number.append(4)
# append() method is used to add an element at the end of the list
number.insert(3, 11)
# insert() method is used to add an element at the specified position in the list
number.pop(1)
# pop() method is used to remove an element at the specified position in the list and return it. If no index is specified, it removes and returns the last item in the list.
print(number)
