"""
Write a class that counts how many instances have been created using a class variable. Add classmethod total_instances() and reset().
"""

class ClassCounter():
  _counter = 0

  def __init__(self):
    ClassCounter._counter += 1

  @classmethod
  def total_instances(cls):
    return cls._counter

  @classmethod
  def reset(cls):
    cls._counter = 0

test1 = ClassCounter()
test4 = ClassCounter()
test2 = ClassCounter()
test3 = ClassCounter()
print(ClassCounter.total_instances())

ClassCounter.reset()

print(ClassCounter.total_instances())