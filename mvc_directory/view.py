
class ContactView:

    @staticmethod
    def hello_start():
        """приветственное сообщение"""
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

    @staticmethod
    def display_contacts(contacts):
        """Показывает список контактов"""
        for idx, user in contacts.items():
            print(f'Пользователь № {idx}')
            for key, value in user.items():
                print(f'\t{key:<10} {value}')
            print()

    @staticmethod
    def new_contact():
        """Добавляет новый контакт"""
        name = input('Введите имя абонента:\n')
        phone = input('Введите номер телефона:\n')
        comment = input('Комментарий к абоненту:\n')
        new_user = {'Имя': name, 'Номер': phone, 'Комментарий': comment}
        print(new_user)
        action_digit_two = input('Сохраняем: \n1)Да\n2)Нет\n')
        if action_digit_two == '1':
            print('Контакт добавлен')
            return new_user
        elif action_digit_two == '2':
            print('Контакт не создан')
            return None
        else:
            print('Ввели не корректное действие')
            return None

    @staticmethod
    def enter_what_or_who_looking_for():
        """Введи что ищешь"""
        return input('Введите слово или номер для поиска:\n')

    def show_search_result(self,found, contact_info):
        """Отображение результата поиска"""
        if found:
            print("Контакт найден:")
            for key, value in contact_info.items():
                print(f"{key}: {value}")
        else:
            print("Контакт не найден")

    @staticmethod
    def change_info():
        key_search = input('Что хотим изменить:')
        value_search = input('На что меняем?')
        action_digit_two = input('Сохраняем: \n1)Да\n2)Нет\n')
        if action_digit_two == '1':
            print("Контаты успешно сохранены")
            return key_search,value_search
        elif action_digit_two == '2':
            print('Контакт не изменен')
            return None,
        else:
            print('Я не нашел ничего')
            return None

    @staticmethod
    def show_not_found_message():
        print("Контакт не найден")

    @staticmethod
    def show_success_message():
        print("Контакт успешно обновлен")

    @staticmethod
    def delete_question():
        action_digit_two = input('Удаляем?\n1)да\n2)нет\n')
        if action_digit_two == '1':
            print('Готов')
        elif action_digit_two == '2':
            print('Окей')
        return action_digit_two

    @staticmethod
    def action_digit_error():
        print('Такого нету, повторите.')