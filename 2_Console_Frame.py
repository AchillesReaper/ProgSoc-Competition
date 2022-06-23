import re

text = input()



x = re.split(" ", text)
longestCount = 0
for i in x:
    if len(i) > longestCount:
        longestCount = len(i)



for i in range(longestCount+4):
    print("*", end='')

print("")
for i in x:
    print("* ", end='')
    print(i,end='')
    for j in range(longestCount-len(i)):
        print(" ",end='')
    print(" *")

for i in range(longestCount+4):
    print("*", end='')


