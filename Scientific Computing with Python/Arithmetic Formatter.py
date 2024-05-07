def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        problems = "Error: Too many problems."
        return problems
    count = 0
    final = ""
    computeArray = []
    #splt numbers into list
    while count < len(problems):
        if "+" in problems[count]:
            split = problems[count].split(" + ")
            split.append("+ ")
            computeArray.append(split)
            tof = computeArray[count][0].isdigit()
            tof2 = computeArray[count][1].isdigit()
            print(tof, tof2)
            if computeArray[count][0].isdigit() == False or computeArray[count][1].isdigit() == False:
                problems = "Error: Numbers must only contain digits."
                return problems
            operation = int(computeArray[count][0]) + int(computeArray[count][1])
        elif "-" in problems[count]:
            split = problems[count].split(" - ")
            split.append("- ")
            computeArray.append(split)
            tof = computeArray[count][0].isdigit()
            tof2 = computeArray[count][1].isdigit()
            print(tof, tof2)
            if computeArray[count][0].isdigit() == False or computeArray[count][1].isdigit() == False:
                problems = "Error: Numbers must only contain digits."
                return problems
            operation = int(computeArray[count][0]) - int(computeArray[count][1])
        else:
            problems = "Error: Operator must be '+' or '-'."
            return problems
        if len(computeArray[count][0]) > 4 or len(computeArray[count][1]) > 4:
            problems = "Error: Numbers cannot be more than four digits."
            return problems
        # difference between two numbers
        firstNum = computeArray[count][0]
        secondNum = computeArray[count][1]
        computeArray[count].append(operation)
        count += 1
    # Finding length of bar

    count = 0
    while count < len(problems):
        firstNum = computeArray[count][0]
        secondNum = computeArray[count][1]
        if len(firstNum) > len(secondNum):
            barLength = len(firstNum) + 2
        else:
            barLength = len(secondNum) + 2
        bar = "-" * (barLength)

        # Find shift for both numbers
        shiftFirst = " " * (barLength - len(str(firstNum)))
        shiftSecond = " " * ((barLength-2) - len(str(secondNum)))
        if count + 1 == len(problems):
            computeArray[count][0] = shiftFirst + firstNum
            computeArray[count][1] = computeArray[count][2] + shiftSecond + secondNum
            computeArray[count].append(bar)
        else:
            computeArray[count][0] = shiftFirst + firstNum + "    "
            computeArray[count][1] = computeArray[count][2] + shiftSecond + secondNum + "    "
            computeArray[count].append(bar + "    ")
        count += 1
    count = 0
    while count < len(problems):
        final = final + computeArray[count][0]
        if count == 0:
            final.strip()
        count += 1
    
    final = final + "\n"
    count = 0

    #adding 2nd line
    while count < len(problems):
        final = final + computeArray[count][1]
        count += 1

    final = final + "\n"
    count = 0
    while count < len(problems):
        final = final + str(computeArray[count][4])
        count += 1
    

    count = 0

    if show_answers==True:
        final = final + "\n"
        count = 0 
        while count < len(problems):
            one = (len(computeArray[count][1]))
            two = (len(str(computeArray[count][3])))
            shiftAnswer = " " * ((one-two) - 4)
            #used for if a number goes up base 10 from addition
            if (len(str(computeArray[count][3]))) + 1 == len(computeArray[count][4]):
                final = final + shiftAnswer + " " + str(computeArray[count][3])
            elif count + 1 == len(problems):
                final = final + shiftAnswer + str(computeArray[count][3])
            else:
                final = final + shiftAnswer + str(computeArray[count][3]) + "    "
            count += 1
    problems = final
    return problems

print((f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}'))
# print(repr("  3801      123\n-    2    +  49\n------    -----"))