# Example 1
class A:
   def a(self):
       return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


class C(B, A):
    pass

class D(A, B):
    pass


# Driver code
c = C()
print('Class C:', c.a())
d = D()
print('Class D:', d.a())
