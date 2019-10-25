"""
_name - private, but it is only convention
__name - name mangling, it will be visible as _ClassName__name
__name__ - python specific methods
"""

class Person:
    def __init__(self):
        self.name = "Phil"
        self._secret = "hello!"
        self.__msg = "mangling message"


p = Person()

print(p.name)
print(p._secret)
print(p._Person__msg)

