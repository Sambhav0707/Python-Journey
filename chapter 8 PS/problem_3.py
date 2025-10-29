l = ["sambhav" , "vaibhav" , "kairav" , "av"]


def rev(list , word):
    n = []
    for w in list:
        if not w == word:
            n.append(w.strip(word))

    return n

print(rev(l , "av"))  



            

    
