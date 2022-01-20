from single2 import C
from single3 import S
class Parent(C,S):
    def function(self):
        print("hello")
y=Parent()
y.function()
y.circle(int(input()))
y.square(int(input()))