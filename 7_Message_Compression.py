text = input()
result = ""

if text[0] == "E":
    # print("encoding")
    repeatConunt = 0
    for i in range(2, len(text)):
        if text[i] == text[i-1]:
            repeatConunt += 1
        else:
            if repeatConunt != 0:
                result += str(repeatConunt)
            result += text[i]
            repeatConunt = 0
    print(result)
elif text[0] == "D":
    # print("decoding")
    for i in range(2, len(text)):
        if text[i].isdigit():
            result += text[i-1] * int(text[i])
        else:
            result += text[i]
    print(result)
