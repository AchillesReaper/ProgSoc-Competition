number = int(input())

# the first loop is the line
# the second loop represent the content of each line
for i in range(number):
    strTemplate = ""
    if i == 0 or i == number - 1:
        for j in range(number):
            strTemplate += "#"
    else:
        for j in range(number):
            if j == 0 or j == i or j == number-i-1 or j == number-1:
                strTemplate += "#"
            else:
                strTemplate += " "

    print(strTemplate)





    # strTemplate = ""
    # for j in range(number):
    #     strTemplate += " "
    #
    # # print(strTemplate)
    #
    # strTemplate[0].replace(" ", "#", 1)
    # strTemplate[-1].replace(" ", "#", 1)
    #
    # if i == 0 or i == number - 1:
    #     for j in range(number):
    #         strTemplate[j].replace(" ", "#", 1)
    # else:
    #     for j in range(number):
    #         if j == i or -(j+1) == i:
    #             strTemplate[j].replace(" ", "#", 1)
    #
    # print(strTemplate)
