class Parent(object):

   def implicit(self):
       print("Parent implicit()")

   def altered(self):
       print("Parent altered()")

class Child(Parent):
   def altered(self):
      print("child  altered()")
      super(Child, self).altered()
      print("child after parent  altered()")


dad = Parent()

dad.implicit() 


son = Child()
son.altered()
