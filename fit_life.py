WATER_PER_KG = 30 # вода на кг
ML_TO_LITERS = 1000 # мл в литры

while True:
    try:
        user_name = input('Добро пожаловать! Как вас зовут? ')
        user_age_input = input('Сколько вам полных лет? ')
        user_age = int(user_age_input)

        user_weight_input = input(
            'Подскажите, пожалуйста, ваш вес в кг? (Например, 60)'
        ) # добавила здесь уточнение. "кг" вынесла в вопрос, чтоб не путало в примере
        user_weight = float(user_weight_input)

        user_height_input = input(
            'Какой у вас рост в метрах (Например, 1.70)'
            ) # аналогично тому, что выше
        user_height = float(user_height_input)

        if user_height <= 0 or user_weight <= 0:
            raise ValueError('Рост и вес должны быть положительными числами.')

        bmi = round(user_weight / (user_height ** 2), 1)
        water_ml = user_weight * WATER_PER_KG
        water_l = round(water_ml / ML_TO_LITERS, 1)

        print(f'Отчет для {user_name}, ({user_age})')
        print(f'Ваш ИМТ {bmi}')
        print(f'Рекомендуемая норма воды {water_l} л')
        print('Расчет окончен. Будьте здоровы!')
        break

    except ValueError as error:
        print(f'Ошибка ввода: {error}. Пожалуйста, проверьте', end=',')
        print(' что ввели все корректно')
