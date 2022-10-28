class A:
       def A(self):
              print('I am A')

class B:
       def A(self):
              print('I am small a')

       def B(self):
              print('I am small B')

class C(A,B):
       def C(self):
              print('I am C')

## C multiple-inherit A and B, but since A is in the left of B,
## so C inherit A and invoke A.A() according to the left-to-right
## sequence.
              
c = C();
c.A()

## To implement C.B(), class A does not have B() method, so
## C inherit B for the second priority. So C.B() actually
## invokes B() in class B.
c.B()
c.C()

b = B()
b.A()
b.B()
#
# a = A()
# a.A()


