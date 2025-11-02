FILENAME = 'authorization.txt'


def authorization():
    login = input('Введите ваш логин: ')
    password = input('Введите ваш пароль: ')
    with open(FILENAME, 'r', encoding='UTF-8') as file:
        user_data = file.read().split('\n')
        for data in user_data:
            if login == data:
                index = user_data.index(data)
                if password == user_data[index + 1]:
                    print('Вы вошли в аккаунт.')
                break
        else:
            raise ValueError('Неверный логин или пароль.')


def registration():
    login = input('Придумайте ваш логин: ')
    if 3 <= len(login) <= 20:
        with open(FILENAME, 'a', encoding='UTF-8') as file:
            file.write(f'\n{login}')
    else:
        raise ValueError('Логин должен быть не менее 3 и не более 20 '
                         'символов.')
    password = input('Придумайте ваш пароль: ')
    if 4 <= len(password) <= 32:
        with open('authorization.txt', 'a', encoding='UTF-8') as file:
            file.write(f'\n{password}')
            print('Аккаунт создан.')
    else:
        raise ValueError('Пароль должен быть не менее 4 и не более 32'
                         ' символов.')


def main():
    open(FILENAME, 'a').close()
    action_choice = input('Если вы хотите авторизоваться, введите 1, если '
                  'зарегистрироваться, введите 2. ')
    if action_choice == '1':
        authorization()
    elif action_choice == '2':
        registration()
    else:
        raise ValueError('Выберите один и предложенных вариантов.')


if __name__ == '__main__':
    main()
