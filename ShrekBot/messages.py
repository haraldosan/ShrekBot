fil = "ballefrans.txt"


with open(fil, "r") as file:
    tekst = file.read()
    newfile = tekst.split("\n")

print(len(newfile))
liste = []

for i in range(len(newfile)):
    if newfile[i] == " " or newfile[i] == "":
        continue
    else:
        liste.append(newfile[i])

count = 0
for elems in liste:
    if count < 25:
        print(elems)
        count += 1
