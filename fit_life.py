

while True:   #будет возвращать к вопросу после ошибки до тех пор пока не напишут правильно
    try: #чтоб при ошибке что-то писало, а не ломалось совсем
        #к имени не считаю нужным принимать только буквы или что-то такое, так как можно ввести не имя, а никнейм
        user_name = input('Добро пожаловать! Как вас зовут? ') #т.е иметь полные возможности для своего имени - круто

        user_age_input = input('Сколько вам полных лет? ')
        user_age = int(user_age_input)

        user_weight_input = input('Подскажите, пожалуйста, ваш вес? (в кг) ')
        user_weight = float(user_weight_input)

        user_height_input = input('Какой у вас рост? (в метрах) ')
        user_height = float(user_height_input)

        if user_height <= 0 or user_weight <= 0:
            raise ValueError('Рост и вес должны быть положительными числами.')
        #здесь расчет индекса массы тела
        bmi = round(user_weight / (user_height ** 2), 1)
        water_ml = user_weight * 30  
        water_l = round(water_ml / 1000, 1)

        print(f'Отчет для {user_name}, ({user_age})')
        print(f'Ваш ИМТ {bmi}')
        print(f'Рекомендуемая норма воды {water_l} л')
        print('Расчет окончен. Будьте здоровы!')
        break 
        
    except ValueError as error:
        print(f'Ошибка ввода: {error}. Пожалуйста, проверьте, что ввели все корректно')
    except Exception as error:
        print(f'Произошла непредвиденная ошибка: {error}')