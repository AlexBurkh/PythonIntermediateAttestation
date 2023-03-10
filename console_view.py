class console_view:
    @staticmethod
    def print_list(list):
        for line in list:
            console_view.print_text(line)
    @staticmethod
    def print_text(text):
        print(text)
    @staticmethod
    def read_text(text = None):
        if text is not None:
            return input(f"{text} > ")
        else:
            return input("> ")
    @staticmethod
    def read_int():
        res = console_view.read_text()
        if res.isdigit():
            return int(res)
        else:
            print("Not a digit")
