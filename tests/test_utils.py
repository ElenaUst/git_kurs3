from funcs import utils


def test_get_date():
    assert utils.get_date('2018-01-26T15:40:13.413061') == '26.01.2018'


def test_mask_from_to_msg():
    assert utils.mask_from_to_msg('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert utils.mask_from_to_msg('Счет 64686473678894779589') == 'Счет **9589'
    assert utils.mask_from_to_msg('Visa Classic 6831982476737658') == 'Visa Classic 6831 98** **** 7658'


def test_filter_and_sort_data():
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
