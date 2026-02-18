#swapping numbers
a,b=int(input('enter the first number:')),int((input('enter the second number:')))
print('orginal number of a={}'.format(a))
print('orginal number of b={}'.format(b))
a,b=b,a
print('swapping number of a={}'.format(a))
print('swapping number of b={}'.format(b))