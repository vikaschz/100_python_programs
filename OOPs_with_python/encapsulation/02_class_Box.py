"""
Make a class Box with a private variable __length.
Add a method to update it only if the value is greater than zero.
"""


class Box:

    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.__length = length  # private

    def set_length(self, new_length):
        if new_length > 0:
            self.__length = new_length
        else:
            print("The length must be greater than zero!")

    def get_length(self):
        return self.__length

    def volume(self):
        return self.width * self.height * self.__length


b1 = Box(3, 6, 9)
b1.set_length(-7)   # invalid
b1.set_length(7)    # valid
print("Length:", b1.get_length())
print("Volume:", b1.volume())
