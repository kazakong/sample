a_three = input()
a_two = input()
a_one = input()
b_three =input()
b_two = input()
b_one = input()

a_total = a_three*3+a_two*2+a_one*1
b_total = b_three*3+b_two*2+b_one*1

if a_total > b_total:
    print('A')
elif a_total < b_total:
    print('B')
else:
    print('T')



