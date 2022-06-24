numline = int(input())

contents = []
for i in range(numline):
    contents.append(input())

match = {}
for j in range(len(contents[0])):
    anchor = contents[0][j]
    indexFound = True
    for i in range(1, numline):
        if contents[i][j] != anchor:
            indexFound = False
            break
    if indexFound:
        match[j] = anchor

ref = -1
refIndex = ""
for item in match:
    if int(match[item]) > ref:
        ref = int(match[item])
        refIndex = item
if ref == -1:
    print("No lock on")
else:
    print(refIndex, ref)
