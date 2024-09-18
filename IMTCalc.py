# Данная программа расчитывает Индекс массы тела по специальной формуле и выводит в ответ оценку этого параметра
# Константы
underweight_border = 18.5
normalweight_border = 25

weight = float(input('Введите вес:'))
height = float(input('Введите рост в метрах (например 1.71):'))
IMT = weight / (height * height) #IMT - Индекс Массы тела

if IMT < underweight_border:
    print("Недостаточная масса")
elif underweight_border <= IMT <= normalweight_border:
    print("Оптимальная масса")
elif IMT > normalweight_border:
    print("Избыточная масса")

formatted_IMT = "{:.0f}".format(IMT) if IMT.is_integer() else round(IMT, 2) # Если во float десятичная часть отсутствует - не выводить десятичную часть. Также округлить до 2 знака если это float.
print(f"Индекс массы тела: {formatted_IMT}")
