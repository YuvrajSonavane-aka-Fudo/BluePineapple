def differbyonebit(num1 , num2):
    binaryDiff = num1^num2

    if str(binaryDiff).count('1') == 1:
        print("Yes")
    else:
        print("No")


differbyonebit(1,2)

    
