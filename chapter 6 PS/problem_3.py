spam = {
    "make a friend": 1,
    "buy now": 1,
    "click this": 1
}

comment = input("enter your comment: ")


if(comment in  spam):
    print("ITS A SPAM")
else:
    print("ITS NOT A SPAM")
