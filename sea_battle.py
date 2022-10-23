import random

true_sight = None
p_turns = []
e_turns = []
enemy_ships = []
player_ships = []
player_taken_places = []
enemy_taken_places = []
player_turn = True
player_setup = True

p_field = [['-'] * 6 for i in range(6)]
e_field = [['-'] * 6 for i in range(6)]

class Ship:

    def __init__(self, rear, middle, front):
        self.rear = rear
        self.middle = middle
        self.front = front

#________________________________Функция, которая случайным образом задает координаты корабля противника________________
    def enemy_set_coords(self):
#________________________________На 3 клетки_____________________________________________________________________
        if self.rear and self.middle and self.front:
            while True:
                check_list = []
                vector = random.randint(1, 2)
                random_height = random.randint(0, 5)
                random_width = random.randint(0, 5)

                self.rear = (random_height, random_width)

                if vector == 1:
                    self.middle = (random_height + 1, random_width)
                    self.front = (random_height + 2, random_width)
                else:
                    self.middle = (random_height, random_width + 1)
                    self.front = (random_height, random_width + 2)

                for items in self.rear, self.middle, self.front:
                    for item in items:
                        check_list.append(item)

                check_list.sort()

                if check_list[-1] < 6:
                    if self.rear not in enemy_ships and self.middle not in enemy_ships and self.front not in enemy_ships:
                        if self.rear not in enemy_taken_places and self.middle not in enemy_taken_places and self.front not in enemy_taken_places:
                            enemy_ships.append(self.rear)
                            enemy_ships.append(self.middle)
                            enemy_ships.append(self.front)

                            break

#_____________________________________На 2 клетки_____________________________________________________________

        elif self.rear and self.middle and self.front == False:
            while True:
                check_list = []
                vector = random.randint(1, 2)
                random_height = random.randint(0, 5)
                random_width = random.randint(0, 5)

                self.rear = (random_height, random_width)

                if vector == 1:
                    self.middle = (random_height + 1, random_width)

                else:
                    self.middle = (random_height, random_width + 1)


                for items in self.rear, self.middle:
                    for item in items:
                        check_list.append(item)

                check_list.sort()

                if check_list[-1] < 6:
                    if self.rear not in enemy_ships and self.middle not in enemy_ships:
                        if self.rear not in enemy_taken_places and self.middle not in enemy_taken_places:
                            enemy_ships.append(self.rear)
                            enemy_ships.append(self.middle)


                            break
#_________________________________________На 1 колетку______________________________________________________________
        elif self.rear and self.middle == False and self.front == False:
            while True:


                random_height = random.randint(0, 5)
                random_width = random.randint(0, 5)

                self.rear = (random_height, random_width)

                if self.rear not in enemy_ships:
                    if self.rear not in enemy_taken_places:
                        enemy_ships.append(self.rear)
                        break


#________________________________Функция ниже позволяет игроку задать положение своих кораблей_________________________
    def player_set_coords(self):
        #____________________________Корабль на 3 клетки_______________________________________
        if self.rear and self.middle and self.front:
            print('Вы задаете координаты вашего корабля на 3 клетки')
            print('Введите начальную точку. Помните, что она НЕ МОЖЕТ БЫТЬ ОТРИЦАТЕЛЬНОЙ.')
            while True:
                check_list = []
                while True:
                    height = input('Координаты по вертикали - ')
                    width = input('Координаты по горизонтали - ')
                    try:
                        height, width = int(height), int(width)
                    except:
                        print('Неверные символы, только цифры. Повторите ввод!')
                    else:
                        if 0 <= height < 6 and 0 <= width < 6:
                            self.rear = (height, width)
                            break
                        else:
                            print(
                                'Одна из ваших введенных точек отрицательна или расположена за пределами доски')
                print(
                    'Теперь выберите между вертикалью(все точки ниже указанной) и горизонаталью(все точки правее указанной)')

                while True:
                    side_choose = input('Ниже|Правее').lower()
                    if side_choose == 'ниже':
                        self.middle = (height + 1, width)
                        self.front = (height + 2, width)
                        break
                    elif side_choose == 'правее':
                        self.middle = (height, width + 1)
                        self.front = (height, width + 2)
                        break
                    else:
                        print('Неверный ввод. Команды отображаются через черточку.')

                for items in self.middle, self.front:

                    for item in items:

                        check_list.append(item)

                check_list.sort()


                if check_list[-1] < 6:
                    if self.rear not in player_ships and self.middle not in player_ships and self.front not in player_ships:
                        if self.rear not in player_taken_places and self.middle not in player_taken_places and self.front not in player_taken_places:
                            player_ships.append(self.rear)
                            player_ships.append(self.middle)
                            player_ships.append(self.front)
                            #return self.rear, self.middle, self.front
                            break
                    else:
                        print('Одна из точек занята!')
                else:
                    print('Одна из точек оказалась за пределами доски! Далее повторите свой ввод заново!')







        #__________________________________Корабль на 2 клетки________________________________________

        elif self.rear and self.middle and self.front == False:
            print('Вы задаете координаты вашего корабля на 2 клетки')
            print('Введите начальную точку. Помните, что она НЕ МОЖЕТ БЫТЬ ОТРИЦАТЕЛЬНОЙ.')

            while True:
                check_list = []
                while True:
                    height = input('Координаты по вертикали - ')
                    width = input('Координаты по горизонтали - ')
                    try:
                        height, width = int(height), int(width)
                    except:
                        print('Неверные символы, только цифры. Повторите ввод!')
                    else:
                        if 0 <= height < 6 and 0 <= width < 6:
                            self.rear = (height, width)
                            break
                        else:
                            print(
                                'Одна из ваших введенных точек отрицательна или расположена слишком близко к краю доски, повторите ввод')
                print(
                    'Теперь выберите между вертикалью(все точки ниже указанной) и горизонаталью(все точки правее указанной)')

                while True:
                    side_choose = input('Ниже|Правее').lower()
                    if side_choose == 'ниже':
                        self.middle = (height + 1, width)
                        break
                    elif side_choose == 'правее':
                        self.middle = (height, width + 1)
                        break
                    else:
                        print('Неверный ввод. Команды отображаются через черточку.')

                for item in self.middle:
                    check_list.append(item)



                check_list.sort()


                if check_list[-1] < 6:
                    if self.rear not in player_ships and self.middle not in player_ships:
                        if self.rear not in player_taken_places and self.middle not in player_taken_places:
                            player_ships.append(self.rear)
                            player_ships.append(self.middle)
                            #return self.rear, self.middle
                            break
                    else:
                        print('Одна из точек занята!')
                else:
                    print('Одна из точек оказалась за пределами доски! Далее повторите свой ввод заново!')


        #_______________________Корабль на 1 клетку_______________________________

        elif self.rear and self.middle == False and self.front == False:
            print('Вы задаете координаты вашего корабля на 1 клетку')
            print('Введите начальную точку. Помните, что она НЕ МОЖЕТ БЫТЬ ОТРИЦАТЕЛЬНОЙ.')

            while True:
                height = input('Координаты по вертикали - ')
                width = input('Координаты по горизонтали - ')
                try:
                    height, width = int(height), int(width)
                except:
                    print('Неверные символы, только цифры. Повторите ввод!')
                else:
                    if 0 <= height < 6 and 0 <= width < 6:
                        self.rear = (height, width)

                    if self.rear not in player_ships and self.rear not in player_taken_places:

                        player_ships.append(self.rear)

                        #return self.rear
                        break

                    else:
                        print('Одна из ваших введенных точек отрицательна или расположена слишком близко к краю доски, или уже занята, или не может быть занята. Повторите ввод')
#______________________________Функция ниже вычисляет запрещенные места для постановки кораблей___________________________
    def calculate_banned_places(self):

        if self.rear and self.middle and self.front:
            for corteg in self.rear, self.middle, self.front:
                banned_item_1 = (corteg[0] + 1, corteg[1])
                banned_item_2 = (corteg[0] - 1, corteg[1])
                banned_item_3 = (corteg[0], corteg[1] + 1)
                banned_item_4 = (corteg[0], corteg[1] - 1)
                if player_setup:
                    player_taken_places.append(banned_item_1)
                    player_taken_places.append(banned_item_2)
                    player_taken_places.append(banned_item_3)
                    player_taken_places.append(banned_item_4)
                else:
                    enemy_taken_places.append(banned_item_1)
                    enemy_taken_places.append(banned_item_2)
                    enemy_taken_places.append(banned_item_3)
                    enemy_taken_places.append(banned_item_4)




        elif self.rear and self.middle and self.front == False:
            for corteg in self.rear, self.middle:
                banned_item_1 = (corteg[0] + 1, corteg[1])
                banned_item_2 = (corteg[0] - 1, corteg[1])
                banned_item_3 = (corteg[0], corteg[1] + 1)
                banned_item_4 = (corteg[0], corteg[1] - 1)
                if player_setup:
                    player_taken_places.append(banned_item_1)
                    player_taken_places.append(banned_item_2)
                    player_taken_places.append(banned_item_3)
                    player_taken_places.append(banned_item_4)
                else:
                    enemy_taken_places.append(banned_item_1)
                    enemy_taken_places.append(banned_item_2)
                    enemy_taken_places.append(banned_item_3)
                    enemy_taken_places.append(banned_item_4)


        elif self.rear and self.middle == False and self.front == False:
            banned_item_1 = (self.rear[0] + 1, self.rear[1])
            banned_item_2 = (self.rear[0] - 1, self.rear[1])
            banned_item_3 = (self.rear[0], self.rear[1] + 1)
            banned_item_4 = (self.rear[0], self.rear[1] - 1)
            if player_setup:
                player_taken_places.append(banned_item_1)
                player_taken_places.append(banned_item_2)
                player_taken_places.append(banned_item_3)
                player_taken_places.append(banned_item_4)
            else:
                enemy_taken_places.append(banned_item_1)
                enemy_taken_places.append(banned_item_2)
                enemy_taken_places.append(banned_item_3)
                enemy_taken_places.append(banned_item_4)



class Board:



    @staticmethod
    def show_player_field():
        print('ВАШЕ ПОЛЕ')
        print(f'  0 1 2 3 4 5')
        for coord in player_ships:
            p_field[coord[0]][coord[1]] = 'F'
        for i in range(6):
            print(f'{i} {p_field[i][0]} {p_field[i][1]} {p_field[i][2]} {p_field[i][3]} {p_field[i][4]} {p_field[i][5]}')


    @staticmethod
    def show_enemy_field():
        print('ПОЛЕ ВРАГА')
        print(f'  0 1 2 3 4 5')
        for i in range(6):
            print(f'{i} {e_field[i][0]} {e_field[i][1]} {e_field[i][2]} {e_field[i][3]} {e_field[i][4]} {e_field[i][5]}')


    @staticmethod
    def player_strike():

        while True:

            p_height_shot = input('Введите координату по вертикали - ')
            p_width_shot = input('Введите координату по горизонтали - ')

            try:
                p_height_shot = int(p_height_shot)
                p_width_shot = int(p_width_shot)
            except:
                print('Вы ввели не числа!')

            else:
                if 0<= p_height_shot < 6 and 0<= p_width_shot <6:
                    if (p_height_shot, p_width_shot) not in p_turns:
                        if (p_height_shot, p_width_shot) in enemy_ships:
                            e_field[p_height_shot][p_width_shot] = 'X'
                            enemy_ships.remove((p_height_shot, p_width_shot))
                            print('Прямое попадание!')
                            p_turns.append((p_height_shot, p_width_shot))

                            return True
                            break

                        else:
                            e_field[p_height_shot][p_width_shot] = '0'
                            p_turns.append((p_height_shot, p_width_shot))
                            return False
                            break
                    else:
                        print('Вы уже стреляли туда!')
                else:
                    print('За пределами доски!')








    @staticmethod
    def ai_strike():
        while True:
            #focus_aim.clear()
            height_shot = random.randint(0, 5)
            width_shot = random.randint(0, 5)


            if (height_shot, width_shot) not in e_turns:
                print('Выстрел ИИ', height_shot, width_shot)
                if (height_shot, width_shot) in player_ships:
                    p_field[height_shot][width_shot] = 'X'
                    player_ships.remove((height_shot, width_shot))
                    print('ИИ поразил ваш корабль!')
                    e_turns.append((height_shot, width_shot))
                    #focus_aim.append(height_shot)
                    #focus_aim.append(width_shot)
                    return True
                    break



                else:
                    p_field[height_shot][width_shot] = '0'
                    e_turns.append((height_shot, width_shot))
                    return False
                    break


board = Board()
#_______________________________Здесь задается флот игрока_______________________________________________
board.show_player_field()

player_cruiser_1 = Ship(True, True,  False)
player_cruiser_1.player_set_coords()
player_cruiser_1.calculate_banned_places()
board.show_player_field()


player_cruiser_2 = Ship(True, True,  False)
player_cruiser_2.player_set_coords()
player_cruiser_2.calculate_banned_places()
board.show_player_field()


player_battleship_1 = Ship(True, True,  True)
player_battleship_1.player_set_coords()
player_battleship_1.calculate_banned_places()
board.show_player_field()




player_boat_1 = Ship(True, False,  False)
player_boat_1.player_set_coords()
player_boat_1.calculate_banned_places()
board.show_player_field()


player_boat_2 = Ship(True, False,  False)
player_boat_2.player_set_coords()
player_boat_2.calculate_banned_places()
board.show_player_field()


player_boat_3 = Ship(True, False,  False)
player_boat_3.player_set_coords()
player_boat_3.calculate_banned_places()
board.show_player_field()

#________________________________Здесь подходит очередь компьютеру задавать свои координаты_____________________________
player_setup = False

enemy_cruiser_1 = Ship(True, True,  False)
enemy_cruiser_1.enemy_set_coords()
enemy_cruiser_1.calculate_banned_places()



enemy_cruiser_2 = Ship(True, True,  False)
enemy_cruiser_2.enemy_set_coords()
enemy_cruiser_2.calculate_banned_places()



enemy_battleship_1 = Ship(True, True,  True)
enemy_battleship_1.enemy_set_coords()
enemy_battleship_1.calculate_banned_places()





enemy_boat_1 = Ship(True, False,  False)
enemy_boat_1.enemy_set_coords()
enemy_boat_1.calculate_banned_places()



enemy_boat_2 = Ship(True, False,  False)
enemy_boat_2.enemy_set_coords()
enemy_boat_2.calculate_banned_places()



enemy_boat_3 = Ship(True, False,  False)
enemy_boat_3.enemy_set_coords()
enemy_boat_3.calculate_banned_places()


print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Добро пожаловать в морской бой. Соломонов Егор FPW 92. Ээм... В свое оправдание миллиардам строчек кода в этой программе
могу сказать лишь... ну зато работает))). Приятной игры. На строчках 504 и 505 есть чит коды, если хотите быстро побе -
дить компьютер и проверить работоспособность программы. Просто активируйте их
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")

while True:


    if player_turn:
        board.show_player_field()
        board.show_enemy_field()
        print('Ваш ход')
        #print('Корабли игрока -', player_ships)
        #print('Корабли компьютера - ', enemy_ships)
        true_sight = board.player_strike()

    else:
        print('Ход ИИ')
        true_sight = board.ai_strike()
        #print('Корабли компьютера - ', enemy_ships)

    if player_ships == []:
        print('Скайнет скоро захватит мир!!!')
        break

    if enemy_ships == []:
        print('Человечество может быть спокойно. Пока-что...')
        break

    if true_sight == False:
        player_turn = False if player_turn else True