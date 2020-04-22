# Omicron35
A work in progress Panda3D game by MaxwellSalmon.

# Documentation
#### Setting up a function that should run when an object is interacted with:

	Simply execute a function with no parameters:

	```object_functions[str(object)] = object_function```

	Execute a function with parameters:

	```object_functions[str(object)] = [object_function, {'a':1, 'b':2, 'c':3}]```

	Function should be defined in **functions.py** and loaded in **models.py**

#### Loading models the fast way
Models can be loaded by using the load_model function. It needs a path or simply just the name of the file.

It can also take keyword arguments being the following:
```
parent = node path
scale = float
pos = tuple 3
hpr = tuple 3
tag = string
function = object_function
```
This is done in script **superloader.py**

#### Creating cutscenes:
```
self.cutscene([self, [{point},{point},{point}]])
```
Points are dictionaries with following keys:
```
x, y, z = world coordinates
h, p, r = object rotation
d = duration
b = blend mode - 'easeIn', 'easeOut', 'noBlend', default is 'easeInOut'
```
Note, that the player's p value can only be between -90 and 90.

This is done in script **main.py**
