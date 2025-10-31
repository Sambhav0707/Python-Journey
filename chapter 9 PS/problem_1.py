'''
Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.
'''

with open("file.txt") as f:
    st = f.read()
    if "twinkle" in st :
      print("present")
    else:
      print("Not Present")

