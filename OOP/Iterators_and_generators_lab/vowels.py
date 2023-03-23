class vowels:
    def __init__(self, string):
        self.string = string
        self.my_list = ["a","e","i","o","u","y"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string)-1:
            raise StopIteration

        self.index += 1
        if self.string[self.index].lower() in self.my_list:
            return self.string[self.index]
        else:
            self.index += 1
            if self.string[self.index].lower() in self.my_list:
                return self.string[self.index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
