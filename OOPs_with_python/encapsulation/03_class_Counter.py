"""
Create a class Counter that keeps a private count variable.
Add methods to increase and view the count.
"""


class Counter:
    def __init__(self):
        self.__count = 0  # private variable

    def increase(self):
        self.__count += 1

    def get_count(self):
        return self.__count


c = Counter()
c.increase()
c.increase()
c.increase()
print(c.get_count())  # 3
