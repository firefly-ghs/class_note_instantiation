import os
class B():
    def __init__(self, path, base):
        self.path = path
        self.base = base
        self.modif = None

    def func2(self):
        if os.path.exists(self.path) is not True:
            os.mkdir(self.path)
        with open(self.path + '/shader.txt', 'w') as f:
            f.write(self.base)
