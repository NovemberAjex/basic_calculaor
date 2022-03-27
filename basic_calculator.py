number_1 = float(input("Please give 1st no:  "))
number_2 = float(input("Please give 2nd no:  "))
choose = int(input("""
Press 1 to add
press 2 to subtract
press 3 multiply
press 4 to divide
"""))
if choose==1:
    print(number_1+number_2)
elif choose == 2:
    print(number_1-number_2)
elif choose ==3:
    print(number_1*number_2)
elif choose ==4:
    print(number_1/number_2)
else:
    print("Try again")