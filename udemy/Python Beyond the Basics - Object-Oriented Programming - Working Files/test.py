#!/usr/bin/python

class MyClass(object):
	var = 10

this_obj = MyClass()
that_obj = MyClass()

print(this_obj)
print(this_obj.var)
print(that_obj.var)


class Joe(object):
	def callme(self):
		print("calling 'callme' method with instance:  ")
		print(self)

thisjoe = Joe()

print(thisjoe.callme())
print(thisjoe)




print("\n")