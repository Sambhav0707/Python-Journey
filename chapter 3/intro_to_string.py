name = "Sambhav"

#slicing the string

a = name[1:6] #this means index 1 is included and index 6 is not included

print(a)

b = name[:6] #this means that it will start from 0 to upto index 6
c = name[1:] #this means that it will start from 1 upto last index

print(b)
print(c)

# there is also a concept of negative slicing 

print(name[-5 : -1]) #if we convert this it will become 2 and upto the last index

#there is also a thing called skipping in the slicing

print(name[0:6 : 2]) #this means we take the string from 0 to 6 and skip 2 chars in it 