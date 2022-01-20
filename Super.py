class A:
    def __init__(self):
        print('Intializing: class A')
    def sub_method(self, b):
        print('Printing from A:',b)
class B(A):
    def __init__(self):
        print('Intializing: class B')
        super().__init__()
    def sub_method(self, b):
        print('Printing from class B:', b)
class C(B):
    def __init__(self):
        print('Intializing: class C')
        super().__init__()
    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b+1)
y=C()
y.sub_method(5)