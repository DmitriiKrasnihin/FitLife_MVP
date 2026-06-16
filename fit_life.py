# Проект FitLife - MVP версия 1.0
ML_PER_L = 1000#Сколько миллилитров в литрах

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
user_name = input('Введите свое Имя\n[- ')
user_age = int(input('Сколько Вам лет\n[- '))


# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
user_weight = float(input('Введите Ваш текущий вес (кг через .)\n[- '))
user_height = float(input('Введите Ваш рост (М через .)\n[- '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)

def bmi_test(user_weight, user_height):
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)



# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def water_test(user_weight):
    water = (user_weight * 30) / ML_PER_L
    return round(water, 1)


# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"Добро пожаловать, {user_name}!")
print(f"Имя: {user_name}\
      \nВозраст: {user_age}\
      \nВаш индекс массы тела: {bmi_test(user_weight, user_height)}\
        \nРекомендуемая норма воды: {water_test(user_weight)} л. в день")
print("Расчет окончен. Будьте здоровы!")