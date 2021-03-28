def data(name, surname, year, city, email, phone):
    '''
    Функция собирает введенные данные пользователя в одну строку и выводит на экран

    :param name: str
    :param surname: str
    :param year: int
    :param city: str
    :param email: str
    :param phone: str
    :return: None
    '''
    print(f'Имя: {name}, фамилия: {surname}; год рождения: {year}, город проживания: {city}, email: {email}, телефон: {phone}')
    return


data(name=input('Введите имя пользователя: '),
     surname=input('Введите фамилию пользователя: '),
     year=int(input('Введите год рождения: ')),
     city=input('Введите город проживания: ') ,
     email=input('Введите email: '),
     phone=input('Введите номер телефона: '))
