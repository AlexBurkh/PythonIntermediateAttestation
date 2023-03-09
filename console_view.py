class console_view:
    def print_list(self, list):
        for line in list:
            self.print_text(line)
    def print_text(self, text):
        print(text)
    def read_text(self, text = None):
        if text is not None:
            return input(f"{text} > ")
        else:
            return input("> ")
    def read_int(self):
        res = self.read_text()
        if res.isdigit():
            return int(res)
