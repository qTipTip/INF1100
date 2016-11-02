### Classes

Given the following class

```
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print self.name, " is ", self.age, " years old!"
```

We can write statements like
```python
test = Person('Lars', 12)
test.info()
```
which yields the output:

```bash
→ python Person.py
Lars  is  12  years old!
```

Consider now what happens if we write only:
```python
print test
```
What is the output?
