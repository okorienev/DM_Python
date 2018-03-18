class Male:
    GENDER = 'male'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Female:
    GENDER = 'female'

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
