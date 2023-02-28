""" 
Associação, uma classe utilizar outra classe mas elas são independentes uma da outra

Association, a class uses another class but they are independent of each other
"""
from classes import Writer
from classes import Pen
from classes import Typewriter
# Test 1
"""
writer = Writer('John')
print(writer.name)

pen = Pen('Bic')
print(pen.brand)

machine = Typewriter()
machine.write()
"""
# Test 2
writer = Writer('John')
pen = Pen('Bic')
machine = Typewriter()

writer.tool = pen
writer.tool.write()
