import string
text = input()
codeDict = dict.fromkeys(string.ascii_letters, 0)
i = 0
for alphabet in codeDict:
    codeDict[alphabet] = i
    i += 1

msg = ""
for i in range(0, len(text), 2):
    x = text[i] + text[i + 1]
    xValue = int(x)
    while xValue > 51:
        xValue -= 52
    # change it to alphabet
    for key in codeDict:
        if codeDict[key] == xValue:
            msg += key
            break

print(msg)
