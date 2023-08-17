import json
from utils import filter_and_sort_data, prepare_user_msg


def main():
    with open('operations.json', "r", encoding='utf-8') as fp:
        data = json.load(fp)
    items = filter_and_sort_data(data)
    for i in range(5):
        print(prepare_user_msg(items[i]))
        print()



if __name__ == '__main__':
    main()
