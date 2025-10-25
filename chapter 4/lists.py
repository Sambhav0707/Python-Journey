#list are a collection of multiple type of data and they are mutable 

l1 = [3,4,5,"sambhav"]

#methods on the list 

#append :- appends a value at the end of the list 

l1.append(7773)

print(l1)

#sort and reverse
l2 = [99,93,29,7]
l2.sort() 

print(l2)

l2.reverse()

print(l2)


#insert :- adding any element at a specific position
l2.insert(3 , 5) #added 5 on index 3 

print(l2)

#remove - will remove the element from the list 

l2.remove(7)
print(l2)

#pop :- will delet the element on the given index and returns a value

print(l2.pop(2))

