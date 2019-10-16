# Python Cars
**Python Cars** is a project I made to strengthen my knowledge of OOP (Object Orientated Programming) composition.   
**Python Cars** consists of 3 python files full of classes that are used within one another to create Car objects.

# Creating Cars
To create a car object, create a new python file in the directory of this project and import the _car.py_ file.

Then, do `car.Car()` to initialize a Car object with default values.   
```Python
import car

defaultCar = car.Car()
```
To define non-default attributes, either pass a kwargs dictionary or define each attribute separately.
```Python
import car

# Defined with dictionary
customCar = car.Car(**{'year': 2015, 'make': 'Mercedes-Benz', 'model': 'SLS AMG GT Black Series'})

# Defined separately
anotherCar = car.Car(make='BMW', model='M3', paddle_shifters=True)
```
