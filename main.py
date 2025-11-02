def main():
    open('authorization.txt', 'a').close()
    main_ = input('Если вы хотите авторизоваться, введите 1, если '
                  'зарегистрироваться, введите 2. ')
    if main_ == '1':
        authorization()
    elif main_ == '2':
        registration()
    else:
        raise ValueError('Выберите один и предложенных вариантов.')


def authorization():
    login = input('Введите ваш логин: ')
    password = input('Введите ваш пароль: ')
    with open('authorization.txt', 'r', encoding='UTF-8') as file:
        text = file.read().split('\n')
        for data in text:
            if login == data:
                index = text.index(data)
                if password == text[index + 1]:
                    print('Вы вошли в аккаунт.')
                    break
        else:
            raise ValueError('Неверный логин или пароль.')


def registration():
    login = input('Придумайте ваш логин: ')
    if 3 <= len(login) <= 20:
        with open('authorization.txt', 'a', encoding='UTF-8') as file:
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


main()