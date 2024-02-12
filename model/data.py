class MyClass:
    def __init__(self):
        self._data = None

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data