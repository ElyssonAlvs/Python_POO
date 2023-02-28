from people import People

# Test 1
"""
p1 = People('Luiz', 29)
p1.eat('Apple')
p1.stop_eat()
p1.eat('Banana')

Luiz is eat a Apple.
Luiz stop eating.      
Luiz is eat a Banana.

-----------------------------------------------
# Test 2
p1 = People('Luiz', 29)
p1.eat('Apple')
p1.stop_eat()
p1.stop_eat()
p1.eat('Banana')

Luiz is eat a Apple.
Luiz stop eating.
Luiz is not eating.
Luiz is eat a Banana.
"""
# Test 3
"""
p1 = People('Luiz', 29)
p1.eat('Apple')
p1.speak('POO')
p1.stop_eat()
p1.speak('POO')
p1.eat('Food')
p1.stop_speak()
p1.speak('food')
"""
# -----------------------------------------------
# Test 4

p1 = People('Luiz', 29)
p2 = People('John', 32)

p1.speak('POO')
p1.speak('Ice')
p1.eat('Food')

print(p1.current_year)
print(p2.current_year)
print(People.current_year)

print(p1.get_current_year())
print(p2.get_current_year())
