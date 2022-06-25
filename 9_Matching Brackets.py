text = input()

# create list with integer representing brackets

bracketList = []

for i in range(len(text)):
    if text[i] == "{":
        bracketList += [3]
    elif text[i] == "[":
        bracketList += [2]
    elif text[i] == "(":
        bracketList += [1]
    elif text[i] == "}":
        bracketList += [-3]
    elif text[i] == "]":
        bracketList += [-2]
    elif text[i] == ")":
        bracketList += [-1]

# the first closing bracket must match the previous bracket on its left
testing = True
while testing:
    if len(bracketList) == 0:
        break
    elif len(bracketList) == 1:
        testing = False
    else:
        for i in range(1, len(bracketList)):
            if bracketList[i] < 0:
                if bracketList[i] + bracketList[i-1] == 0:
                    del bracketList[i]
                    del bracketList[i-1]
                    break
                else:
                    testing = False

if testing:
    print("yes")
else:
    print("no")
