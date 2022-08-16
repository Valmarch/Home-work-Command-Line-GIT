stars = int(input('Введіть кількість сходинок '))
stairs = ''
for i in range(1, stars+1):
    stairs += '*'
    print(stairs)


stars = int(input('Введіть кількість сходинок '))
start = 0
stairs = ''
while start != stars:
    stairs += '*'
    print(stairs)
    start +=1