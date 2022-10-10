print('Крестики-нолики')

x_turn = None #Типа переменная расшифровывается, как ход крестиков, True Или False

a,b,c,d,e,f,g,h,i = 'a','b','c','d','e','f','g','h','i'

win_combo = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [g, e, c]]

turn_script = []

count = 0

possible_turn = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i' ] #Защита от непредвиденных действий пользователя

breaker = False

while True:

    # Стандартный цикл, где я определяю переменную x_turn
    setupper = input('Кто ходит первым Крестики|Нолики - ').lower()
    if setupper == 'крестики':
        x_turn = True
        break
    elif setupper == 'нолики':
        x_turn == False
        break
    else:
        print('Неверный ввод')

# Переменная задана, теперь основа игрового движка,






while True:
    breaker = False

    setupper = input("""
Rules - правила

>    
    
""").lower()
    # переназначаю переменную Setupper
    # Теперь задаю цикл, где будет три условия, которые выполняют команды выше,
    # и одно исключающее для неверной команды

    setupper = setupper.replace(' ', '')
    setupper = setupper.replace('\n', '')


    if setupper == 'start':
        while True:
            if breaker == True:
                break
            # Сообщение при начале хода, которое говорит, кто ходит сейчас

            if x_turn:
                print('Ходят крестики')

            else:
                print('Ходят нолики')



            while True:

                # Игровое поле
                print(
                    f"""

                              0 1 2
                            0 {a} {b} {c}
                            1 {d} {e} {f}
                            2 {g} {h} {i}

                            """)



                actual_turn = input(f"""
                            Введите букву, куда будет поставлен символ:
                            {'=' * 9}
                            {'Крестики' if x_turn else 'Нолики'}
                            {'=' * 9}

                            """).lower()
                if actual_turn in possible_turn:
                    # Проверка на предыдущие ходы

                    if actual_turn not in turn_script:
                        turn_script.append(actual_turn)

                        # Изменения в графическом интерфейсе

                        if actual_turn == 'a':
                            a = 'x' if x_turn else 'o'
                        if actual_turn == 'b':
                            b = 'x' if x_turn else 'o'

                        if actual_turn == 'c':
                            c = 'x' if x_turn else 'o'

                        if actual_turn == 'd':
                            d = 'x' if x_turn else 'o'

                        if actual_turn == 'e':
                            e = 'x' if x_turn else 'o'

                        if actual_turn == 'f':
                            f = 'x' if x_turn else 'o'

                        if actual_turn == 'g':
                            g = 'x' if x_turn else 'o'

                        if actual_turn == 'h':
                            h = 'x' if x_turn else 'o'

                        if actual_turn == 'i':
                            i = 'x' if x_turn else 'o'


                        #Проверка победы

                        win_combo = [[a,b,c], [d,e,f], [g,h,i], [a,d,g], [b,e,h], [c,f,i], [a,e,i], [g,e,c]]



                        for item in win_combo:
                            if item == ['x', 'x', 'x']:
                                print("Победили крестики")

                                print('Новый раунд!')
                                a, b, c, d, e, f, g, h, i = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
                                turn_script = []

                                breaker = True
                                break

                        for item in win_combo:
                            if item == ['o', 'o', 'o']:
                                print("Победили нолики")

                                print('Новый раунд!')
                                breaker = True
                                a, b, c, d, e, f, g, h, i = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
                                turn_script = []
                                break

                        for item in turn_script:
                            count += 1
                            if count > 8 and breaker == False:
                                print('Ничья')
                                breaker = True
                                a, b, c, d, e, f, g, h, i = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
                                turn_script = []

                        count = 0


                        # Переназначение хода

                        x_turn = False if x_turn else True

                        break





                    else:
                        print('Место занято!')
                else:
                    print('Неверный ввод!!')
    elif setupper == 'quit':
        break

    elif setupper == 'rules':
        ###Блок с правилами
        print("""
Команды:
1. Start - начать игру
2. Quit - остановить программу
3. Rules - список команд и правила    

Перед вами появится поле, введите букву, вместо которой вы хотите поставить ваш символ    
    """)

    else:
        print('Неверная комманда')


