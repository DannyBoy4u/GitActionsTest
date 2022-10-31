class ComboBoxOption:
    """
    This class contains all properties and methods for a ComboBox list item.

    :param str display_text: The display text of the option
    :param str value: The value of the option
    """

    def __init__(self, display_text: str, value: str):
        self.display_text = display_text
        self.value = value

    def superFoo():
        return 1

    def regularFoo(num: int):
        num = (5-num)
        return num
    
    def peasant():
        return "Yee art thou a Peasant"

    def knight():
        return "You are a knight sire"

    def pawn():
        return "You are just a pawn"
    
    def hope():
        return "You must have faith"

    def castle():
        return "This is a castle"