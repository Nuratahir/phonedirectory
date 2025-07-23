class ActionDigitError(Exception):
    def __init__(self, action_digit):
        super().__init__()
        self.action_digit = action_digit
    def __str__(self):
        return 'Нужно ввести число от 1 до 6'


