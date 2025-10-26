
dic = {
    "name" : "Sambhav",
    "DOB" : "07 th Jan",
    "Fav Num" : 7
}

#update :- update the key's value 

dic.update({
    "name" : "sambhav07"
})

print(dic.items()) #items print the key value pairs in the form of list and each in the form of tuple

#keys and values :-

print(dic.keys())
print(dic.values())

#get :- returns non if not found other wise same as using :- dic["name"]

print(dic.get("name1")) #it will return none
# print(dic["name1"]) #this will throw error 