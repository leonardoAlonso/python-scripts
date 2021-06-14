import random
from functools import reduce

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        self.capacity = capacity
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __setrandom__(self, min, max):
        self.items = [random.randint(min, max) for i in range(self.capacity)]

    def __sum__(self):
        return reduce(lambda a, b: a+b, self.items)

class Array2D:

    def __init__(self, rows, cols, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(cols, fill_value)

    def get_heigth(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_heigth()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return result

class Array3D:

    def __init__(self, rows, cols, depth, fill_value=None):
        self.data = Array2D(rows, cols, fill_value)
        self.rows = rows
        self.cols = cols
        self.depth = depth
        for row in range(rows):
            for col in range(cols):
                self.data[row][col] = Array(depth, fill_value)

    def __str__(self):
        result = ""
        for cube in self.data:
            result += str(cube) + "\n"
        return result

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def get_depth(self):
        return len(self.data[0][0])

    def add_numbers(self):
        self.data = [
            [[random.randint(1,20) for i in range(self.depth)]
            for _ in range(self.cols)] for _ in range(self.rows)
        ]


if __name__ == '__main__':
    menu = Array(5)
    menu.__setitem__(0, 100)
    print(menu)
    menu.__setrandom__(0, 100)
    print(menu)
    print(menu.__sum__())

    array2d = Array2D(3, 3)
    print(array2d)

    for row in range(array2d.get_heigth()):
        for col in range(array2d.get_width()):
            array2d[row][col] = row * col
    print(array2d)
    print(array2d.__getitem__(1)[0])
    print(array2d.__str__())

    cube = Array3D(3,3,3)
    print(cube)
    cube.add_numbers()
    print(cube)
