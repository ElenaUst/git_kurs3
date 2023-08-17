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
        account = '**' + str(list_msg[len(list_msg) - 1][-4:])
        mask_msg = 'Счет' + ' ' + account
    else:
        account = str(list_msg[len(list_msg) - 1][0:4]) + ' ' + str(
            list_msg[len(list_msg) - 1][4:6]) + '**' + ' ' + '****' + ' ' + str(list_msg[len(list_msg) - 1][-4:])
        mask_msg = ' '.join((list_msg[:-1])) + ' ' + account
    return mask_msg


def filter_and_sort_data(data):
    """
    Фильтрует транзакции по EXECUTED, получает список успешных транзакций, отсортированный по дате
    :param data: начальный список данных, полученный из файла json
    :return: список, содержащий только успешные транзакции, отсортированный по дате, начиная с последней
    """
    modify_data = []
    for el in data:
        if el.get('state') == 'EXECUTED':
            modify_data.append(el)
            modify_data_1 = sorted(modify_data, key=lambda x: x['date'], reverse=True)
    return modify_data_1


def prepare_user_msg(operation):
    """
    Формирует итоговое сообщение пользователю по операции в заданном формате.
    # Пример вывода для одной операции:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    """

    date = get_date(operation.get('date'))
    desc = operation.get('description')
    if operation.get('from') is None:
        from_ = ''
    else:
        from_ = mask_from_to_msg(operation.get('from'))
    if operation.get('to') is None:
        to_ = ''
    else:
        to_ = mask_from_to_msg(operation.get('to'))
    amount = operation.get('operationAmount').get('amount')
    currency = operation.get('operationAmount').get('currency').get('name')
    return f'{date} {desc}\n{from_} -> {to_}\n{amount} {currency}\n'
