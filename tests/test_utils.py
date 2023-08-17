from funcs import utils


def test_get_date():
    """
    Тестирует функцию перевода даты в формат ДД.ММ.ГГГГ
    """
    assert utils.get_date('2018-01-26T15:40:13.413061') == '26.01.2018'


def test_mask_from_to_msg():
    """
    Тестирует функцию маскировки номера счета/карты для полей <откуда>, <куда>.
    """
    assert utils.mask_from_to_msg('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert utils.mask_from_to_msg('Счет 64686473678894779589') == 'Счет **9589'
    assert utils.mask_from_to_msg('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'


def test_filter_and_sort_data():
    """
    Тестирует функцию отбора успешных транзакций и их сортировки от последней до первой
    """
    assert utils.filter_and_sort_data([{
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2018-12-28T23:10:35.459698"
    },
    {
    "id": 476991061,
    "state": "CANCELED",
    "date": "2018-11-23T17:47:33.127140"
    },
    {
    "id": 633268359,
    "state": "EXECUTED",
    "date": "2019-07-12T08:11:47.735774"
    }]
    ) == [{
    "id": 633268359,
    "state": "EXECUTED",
    "date": "2019-07-12T08:11:47.735774"
    },
    {
    "id": 172864002,
    "state": "EXECUTED",
    "date": "2018-12-28T23:10:35.459698"
    }]


def test_prepare_user_msg():
    """
    Тестирует функцию подготовки сообщения для пользователя в заданном формате
    """
    assert utils.prepare_user_msg({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
    }
) == '26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n'
    assert utils.prepare_user_msg({
    "id": 587085106,
    "state": "EXECUTED",
    "date": "2018-03-23T10:45:06.972075",
    "operationAmount": {
      "amount": "48223.05",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 41421565395219882431"
  }
) == '23.03.2018 Открытие вклада\n -> Счет **2431\n48223.05 руб.\n'
    assert utils.prepare_user_msg({
    "id": 179194306,
    "state": "EXECUTED",
    "date": "2019-05-19T12:51:49.023880",
    "operationAmount": {
      "amount": "6381.58",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "МИР 5211277418228469",
      }
) == '19.05.2019 Перевод организации\nМИР 5211 27** **** 8469 -> \n6381.58 USD\n'
