


with open("donkey.txt") as f:
    content = f.read()

    newContent = content.replace("Donkey" , "#####")

    with open("donkey.txt" , "w") as f:
        f.write(newContent)

