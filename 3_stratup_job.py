import re
text = input()

x = re.split(" ", text)
y = [x[0]]
for i in x:
    if i not in y:
        y.append(i)

for item in y:
    print(item, end=' ')


