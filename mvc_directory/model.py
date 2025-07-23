class ContactModel:

    def __init__(self, filename = 'data_base.txt'):
        self.filename = filename
        self.users = {}
        self.current_contact = None

    def load_contacts(self):
        with open('data_base.txt', 'r', encoding='UTF-8') as file:
            self.users = {}
            data = [item.strip().split(':') for item in file.readlines()]
            for i, item in enumerate(data, 1):
                self.users[i] = {'Имя': item[0].strip(), 'Телефон': item[1].strip(), 'Комментарий': item[2].strip()}

    @staticmethod
    def new_contacts(new_user):
        """Добавляет новый контакт"""
        great_format_contact = list(new_user.values())
        with open('data_base.txt', 'a', encoding='UTF-8') as file:
            file.write('\n')
            file.write(great_format_contact[0])
            file.write(':')
            file.write(great_format_contact[1])
            file.write(':')
            file.write(great_format_contact[2])

    def search_contact_model(self,search_word):
        """Ищем контакт"""
        search_word = str(search_word)
        for i, item in self.users.items():
            for key, value in item.items():
                if search_word == str(value):
                    return True, item, i
        return False, None

    def update_a_contact(self,search_key, search_value):
        if self.current_contact:
            self.current_contact[search_key] = search_value
            with open('data_base.txt', 'w', encoding='UTF-8') as file:
                lines = []
                for i, user in self.users.items():
                    line = f"{user['Имя']}:{user['Телефон']}:{user['Комментарий']}"
                    lines.append(line)
                file.write("\n".join(lines))
                return True
        return False

    def delete(self, action_digit, i):
        users_to_remove = []
        if action_digit == '1':
            users_to_remove.append(i)
            for i in users_to_remove:
                del self.users[i]
            with open('data_base.txt', 'w', encoding='UTF-8') as file:
                contact_list = []
                for i, user in self.users.items():
                    updated_contacts = f'{user['Имя']}:{user['Телефон']}:{user['Комментарий']}'
                    contact_list.append(updated_contacts)
                file.write('\n'.join(contact_list))
        if action_digit == '2':
            return None
