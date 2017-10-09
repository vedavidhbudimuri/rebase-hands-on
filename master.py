"""
Master module
"""


class MyClass(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '%s@%i' % (self.name, self.age)

    def __unicode__(self):
        return '%s@%i' % (self.name, self.age)


def my_function():
    print('My very first function')


if __name__ == '__main__':
    print('Hello World')
    my_function()
    obj = MyClass('Rahul', 21)
    print obj