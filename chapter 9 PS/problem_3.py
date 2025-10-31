


def generateTable(i):
    table = ""
    for t in range(1,11):
        table += f"{i} X {t} = {i*t}\n"

    with open(f"tables/table{i}.txt" , "w") as f:
        f.write(table)    






for i in range(2,21):
    generateTable(i)