class Norm:

    desc = ''
    def __init__(self, env):
        self.env = env
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def check(self, **kwargs):
        pass