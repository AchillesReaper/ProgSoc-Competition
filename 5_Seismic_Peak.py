import re

text = input()

x = re.split(" ", text)

eCount = 0
peakCount = 0
for i in range(1,len(x)-1):
    if peakCount == 1:
        eCount += 1

    if int(x[i]) > int(x[i + 1]) and int(x[i]) > int(x[i - 1]):
        peakCount += 1

print(eCount-1)



