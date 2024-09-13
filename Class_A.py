from Class_B import B
class A():
    def __init__(self, path, base, single_inst):
        self.__path   = path
        self.__single_inst = single_inst  
        self.__base   = base


        self.__generator = None
    
    def func1(self):
        if not self.__generator:
            self.__generator = B(self.__path, self.__base)
        self.__generator.func2()
