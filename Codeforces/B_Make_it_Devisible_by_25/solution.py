tests = int(input())
for test in range(tests):
    #print("new test")
    n = [int(x) for x in input()]
    zero = False
    zero_yes = False
    zero_c = 0
    five = False
    five_yes = False
    five_c = 0
    for i in range(len(n)-1, -1, -1):
        
        c = n[i]

        if five and (c == 2 or c == 7):
            five_yes = True
        elif five and not five_yes:
            five_c += 1
        
        if zero and (c == 0 or c == 5):
            zero_yes = True
        elif zero and (not zero_yes):
            zero_c += 1


        if (not zero) and c == 0:
            zero = True
        elif not zero:
            zero_c +=1
        if (not five) and c == 5:
            five = True
        elif not five:
            five_c += 1
        #print("round", i)
        #print("0:", zero, zero_c, zero_yes)
        #print("5:", five, five_c, five_yes)
    if not five_yes:
        print(zero_c)
    elif not zero_yes:
        print(five_c)
    else:
        print(min(five_c, zero_c))
