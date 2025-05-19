from fileinput import close
from re import search

print('Приветствую тебя, мой дорогой пользователь! '
      'Это мой (автор Нуртахир), телефонный справочник. '
      'Вот его функции:'
      '\n 1. Показать все контакты '
      '\n 2. Создать контакт'
      '\n 3. Найти контакт'
      '\n 4. Изменить контакт'
      '\n 5. Удалить контакт'
      '\n 6. Выход из справочника'
      )
action_digit = input('Введите цифру действия:')

with open ('telephone_friend.txt', 'r', encoding='UTF-8') as file:
        users = {}
        data = [item.strip().split(':') for item in file.readlines()]
        for i, item in enumerate (data,1):
            users[i] = {'Имя': item[0].strip(),'Телефон': item[1].strip(), 'Комментарий': item[2].strip()}


# if action_digit == '1':
''' функция которая показывает все контакты '''
def open_all_contact():
      for idx, user in users.items():
            print(f'Пользователь № {idx}')
            for key, value in user.items():
                  print(f'\t{key:<10} {value}')
            print()

#if action_digit == '2':
''' функция которая добавляет новый контакт '''
def add_new_contact():
      name = input('Введите имя абонента:\n')
      phone = input('Введите номер телефона:\n')
      comment = input('Комментарий к абоненту:\n')
      new_user = {'Имя': name, 'Номер': phone, 'Комментарий':comment}
      print(new_user)
      action_digit_two = input('Сохраняем: \n1)Да\n2)Нет\n')
      if action_digit_two == '1':
            great_format_contact = list(new_user.values())
            with open('telephone_friend.txt', 'a', encoding='UTF-8') as file:
                  file.write('\n')
                  file.write(great_format_contact[0])
                  file.write(':')
                  file.write(great_format_contact[1])
                  file.write(':')
                  file.write(great_format_contact[2])
                  print("Контакт добавлен")
      elif action_digit_two == '2':
            print('Контакт не создан')
      else:
            print('Ввели не корректное действие')

#if action_digit == '3':
''' функция для поиска контакта '''
def search_contact():
      search_word = input('Введите слово или номер для поиска:\n')
      found = False
      for i, item in users.items():
            for key, value in item.items():
                  search_info_contact = list(item.values())
                  if search_word == value:
                        print(f'Я нашел!\n', *search_info_contact[:])
                        found = True
      if not found:
            print('Я не нашел ничего')

#if action_digit == '4':
'''функция для изменения контакта'''
def change_contact():
      search_word = input('Введите имя контакта, которое хотите изменить:\n')
      found = False
      for i, user in users.items():
            for key, value in user.items():
                  if search_word == value:
                        print(f'Нашел такое имя:{user}')
                        found = True
                        key_search = input('Что хотим изменить:')
                        user[key_search] = input('На что меняем?')
                        action_digit_two = input('Сохраняем: \n1)Да\n2)Нет\n')
                        if action_digit_two == '1':
                              with open('telephone_friend.txt', 'w', encoding='UTF-8') as file:
                                          lines = []
                                          for i, user in users.items():
                                                line = f"{user['Имя']}:{user['Телефон']}:{user['Комментарий']}"
                                                lines.append(line)
                                          file.write("\n".join(lines))
                              print("Контаты успешно сохранены")
      if not found:
            print('Я не нашел ничего')

#if action_digit == '5':
'''функция для удаления контакта'''
def delete_contact():
    search_word = input('Введите имя контакта, которое хотите удалить:\n')
    found = False
    users_to_remove = []
    for i, user in users.items():
        for key, value in list(user.items()):
            if search_word == value:
                print(f'Нашел такое имя:{user}')
                found = True
                action_digit_two = input('Удаляем?\n1)да\n2)нет\n')
                if action_digit_two == '1':
                    users_to_remove.append(i)
                    break # выходим из внутреннего цикла после добавления в users_to_remove

    # Удаляем пользователей после завершения итерации
    for i in users_to_remove:
        del users[i]

    # Записываем обновленные данные в файл, только если были удаления
    if found:
        with open('telephone_friend.txt', 'w', encoding='UTF-8') as file:
            contact_list = []
            for i, user in users.items():
                updated_contacts = f'{user['Имя']}:{user['Телефон']}:{user['Комментарий']}'
                contact_list.append(updated_contacts)
            file.write('\n'.join(contact_list))  # Записываем с разделителями

    if not found:
        print('Я не нашел ничего')

if action_digit == '1':
    open_all_contact()
if action_digit == '2':
    add_new_contact()
if action_digit == '3':
    search_contact()
if action_digit == '4':
    change_contact()
if action_digit == '5':
    delete_contact()


while action_digit != '6':
    action_digit = input('Введите цифру для продолжения (выход из справочника, цифра 6):')
    if action_digit == '1':
        open_all_contact()
    if action_digit == '2':
        add_new_contact()
    if action_digit == '3':
        search_contact()
    if action_digit == '4':
        change_contact()
    if action_digit == '5':
        delete_contact()
else:
    print('Пока')