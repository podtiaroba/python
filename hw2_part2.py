# Выбрать рекомендуемую секцию согласно возрасту ребенка.

old = int(input('Сhild age: '))
print('Recommend: ')
if old < 5:
    print('Play sports early') 
elif 5 <= old < 7:
    print('Gymnastics')   
elif 7 <= old < 12:
    print('Athletics')
elif 12 <= old < 16:
    print('Swimming')
else:
    print('All sports')