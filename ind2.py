sentence = input("Введите предложение: ")
for i in range(len(sentence)-1):
    if sentence[i] == sentence[i+1]:
        print("Порядковые номера первой пары одинаковых соседних символов:", i+1, i+2)
else:
    print("Одинаковые соседние символы не найдены.")