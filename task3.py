m = input('Введіть кількість хвилин ')
if m.isdigit() == False:
 print('Помилка')
 exit()
else:m = int(m)

if m < 15:
    print('У першій чверті години')
elif m  >=15 and m < 30:
    print('У другій чверті години')
elif m >= 30 and m < 45:
    print('У третій чверті години')
elif m >= 45 and m < 59:
    print('У останній чверті години')