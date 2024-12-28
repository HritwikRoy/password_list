import random
number=int(input("Enter any number : "));
f=open('file4.txt', 'a')

for i in range(0,number):

    pass1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pass2="abcdefghijklmnopqrstuvwxyz"
    pass3="!@#$%^&*~"
    pass4="1234567890"

    ran_number1=random.randint(0, 25)
    ran_number1_1=random.randint(0, 25)
    ran_number2=random.randint(0, 25)
    ran_number2_2=random.randint(0, 25)
    ran_number3=random.randint(0, 8)
    ran_number3_3=random.randint(0, 8)
    ran_number4=random.randint(0, 9)
    ran_number4_4=random.randint(0, 9)

    result=(pass1[ran_number1],pass3[ran_number3],pass2[ran_number2],pass4[ran_number4],pass3[ran_number3_3],pass2[ran_number2_2],pass1[ran_number4_4],pass4[ran_number3_3],pass1[ran_number1_1],pass4[ran_number4_4])
    output = "".join(result) + '\n'

    f.write(output)

