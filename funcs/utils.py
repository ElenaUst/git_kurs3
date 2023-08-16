from datetime import datetime


def get_date(dt):
    """
    Возвращает дату в формате ДД.ММ.ГГГГ
    """
    return datetime.fromisoformat(dt).strftime('%d.%m.%Y')


def mask_from_to_msg(msg):
    """
    Скрывает номер счета/карты для полей <откуда>, <куда>.
    Номер карты замаскирован и не отображается целиком в формате  XXXX XX** **** XXXX
    Номер счета замаскирован и не отображается целиком в формате  **XXXX
    """
    list_msg = msg.split()
    if list_msg[0] == 'Счет':
        account = '**' + str(list_msg[len(list_msg)-1][-4:])
        mask_msg = 'Счет' + ' ' + account
    else:
        account = str(list_msg[len(list_msg)-1][0:4]) + ' ' + str(list_msg[len(list_msg)-1][4:6]) + '**' + ' ' + '****' + ' ' + str(list_msg[len(list_msg)-1][-4:])
        mask_msg = ' '.join((list_msg[:-1])) + ' ' + account
    return mask_msg


print(mask_from_to_msg("Счет 3152479541115065"))


