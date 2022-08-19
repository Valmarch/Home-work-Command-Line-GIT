months = {'Зима' : [1, 2, 12],
        'Весна' : [3, 4, 5],
        'Літо' : [6, 7, 8],
        'Осінь' : [9, 10, 11]
}
month = int(input('Введіть номер місяця '))
def num_of_mon(months, value):
    for key in months.keys():
        if value in months[key]:
            print(key)


num_of_mon(months, month)



