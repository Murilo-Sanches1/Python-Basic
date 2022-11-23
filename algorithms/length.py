# Eu sei que existe a função len(array: list) que retorná o comprimento do array
# Quero recriar a lógica por trás dessa função

class len(list):
    counter = 0

    def __init__(self):
        super().__init__()

    def length(self, array: list):
        for _ in array:
            self.counter += 1
        return self.counter


#t: len = [1, 2, 3]
# print(t.length())


p = [1, 2, 3]


def length(array: list):
    c = 0
    for _ in array:
        c += 1
    return c


print(length(p))
