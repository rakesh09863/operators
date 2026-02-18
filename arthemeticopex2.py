#program for showing displaying the currency in trems of number of notes
a=int(input('Enter the withdraw amount:'))
#how many notes 500 to be given
n500=a//500
a=a%500
#How many notes 200 to be given
n200=a//200
a=a%200
#How many notes 100 to be given
n100=a//100
a=a%100
print('number of 500 notes={}'.format(n500))
print('number of 200 notes={}'.format(n200))
print('number of 100 notes={}'.format(n100))
