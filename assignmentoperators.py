a=10#single line assignment
b=20
c=a+b
print('{}+{}={}'.format(a,b,c))
print('-'*50)
a,b=int(input('enter the first value:')),int(input('enter the second value:'))#multi line assignment
c,d,e=a+b,a-b,a*b
print('{}+{}={}'.format(a,b,c))
print('{}-{}={}'.format(a,b,d))
print('{}*{}={}'.format(a,b,e))