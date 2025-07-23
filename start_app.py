from mvc_directory.view import ContactView
from mvc_directory.model import ContactModel
from mvc_directory.controller import ContactConrtoll
from mvc_directory.exсeption import ActionDigitError

def main():
    model = ContactModel()
    view = ContactView()
    controller = ContactConrtoll(model,view)
    view.hello_start()
    model.load_contacts()


    while True:
        action_digit = input('Введите цифру действия:')
        if action_digit == '6':
            print('Good Bye')
            break
        try:
            action_digit_int = int(action_digit)
            if action_digit_int == 1:
                controller.open_all_contact()
            elif action_digit_int == 2:
                controller.add_new_contact()
            elif action_digit_int == 3:
                controller.search_contact()
            elif action_digit_int == 4:
                controller.change_contact()
            elif action_digit_int == 5:
                controller.delete_contact()

            # Давай сделаем, что если тут число отрицательное или больше >6,
            # то здесь будет кастомная ошибка
            # if int(action_digit) >= 7:
            #     view.action_digit_error()
            elif 0 <= action_digit_int >= 7:
                raise ActionDigitError(action_digit)
        except ValueError:
            print('Пожалуйста, введите числовое значение.')
        except ActionDigitError as e:
            print(e)

if __name__ == '__main__':
    main()




