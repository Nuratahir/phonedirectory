from mvc_directory.model import ContactModel
from mvc_directory.view import ContactView

class ContactConrtoll:

    def __init__(self,model: ContactModel, view: ContactView):
        self.model : ContactModel = model
        self.view : ContactView = view

    def open_all_contact(self):

        contacts = self.model.users
        self.view.display_contacts(contacts)

    def add_new_contact(self):
        # тут получаем данные от модели view.py
        new_user = self.view.new_contact()
        # проверка, что данные пришли
        if new_user is not None:
            self.model.new_contacts(new_user)
        else:
            pass

    def search_contact(self):
        search_word = self.view.enter_what_or_who_looking_for()
        found, contact_info = self.model.search_contact_model(search_word)
        self.view.show_search_result(found,contact_info)

    def change_contact(self):
        search_word = self.view.enter_what_or_who_looking_for()
        found, contact_info = self.model.search_contact_model(search_word)
        self.view.show_search_result(found,contact_info)
        if found:
            key_search, value_search = self.view.change_info()
            if key_search and value_search:
                # Сохраняем найденный контакт в модель
                self.model.current_contact = contact_info
                self.model.update_a_contact(key_search, value_search)
                self.view.show_success_message()
            else:
                self.view.show_not_found_message()

    def delete_contact(self):
        search_word = self.view.enter_what_or_who_looking_for()
        found, contact_info, i = self.model.search_contact_model(search_word)
        self.view.show_search_result(found, contact_info)
        action_digit = self.view.delete_question()
        self.model.delete(action_digit,i)

