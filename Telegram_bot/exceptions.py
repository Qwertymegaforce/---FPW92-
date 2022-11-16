from config import *

class BotError(Exception):

    @staticmethod
    def check(fsym, tsym, multiplier):
        try:
            float(multiplier)
        except ValueError:
            raise BotError(f'Это не похоже на цифру -  ""{multiplier}"" ⁉️')

        if fsym not in values:
            raise BotError(f'Неправильно введена валюта - ""{fsym}"" ⁉️')

        if tsym not in values:
            raise BotError(f'Неправильно введена валюта - ""{tsym}"" ⁉️' )

    @staticmethod
    def check_schedule(message):
        try:
            int(message)
        except ValueError:
            raise BotError('Неверный ввод группы ⁉️')




