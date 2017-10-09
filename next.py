"""
    Next module
"""


class NextClass(object):
    """
        This is a sample class to create
    """
    def __init__(self, *args, **kwargs):
        self._value = kwargs.get('value', 'value')

    @property
    def value(self):
        return self._value
