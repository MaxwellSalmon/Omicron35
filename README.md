# Omicron35
A work in progress Panda3D game by MaxwellSalmon.
![What it looks like so far](https://i.imgur.com/QqMewsN.png)

# Documentation
Note, that this may not be accurate, as the system is still in development and might have changed. Let me know if you spot an error. Also, I am not
used to writing documentation and mainly did this for my own sake, so feel free to request improvements. 
### Setting up a function that should run when an object is interacted with:

Simply execute a function with no parameters:

```object_functions[obj name] = object_function```

Execute a function with parameters:

```object_functions[obj name] = [object_function, {'a':1, 'b':2, 'c':3}]```

Function should be defined in **functions.py** and loaded when creating a model.

### Loading models the fast way
Models are tied to a scene and automatically loaded when the scene is loaded. The only argument is a path or simply just the name of the file.
It can also take keyword arguments being the following:

```
name = string
scale = float
pos = tuple 3
hpr = tuple 3
tag = string
function = object_function
culling = string
solid = boolean
audio = string
```
The keyword, ```name``` is only necessary, for interactive models, if there are multiple objects sharing the same 3D-model.<br>
This is done in the script **scene_setup.py**

An example for loading an interactive model, which changes the scene can be seen here:
```
Model('door', name='ext_door', tag='interactive', pos=(14,1.35,0.4), scale=0.5, solid=True, culling='both'
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1'}])
```

### Creating scenes:
A scene consists of base elements and scene-specific elements. The base elements are the scene model and its colliders. To create a scene, add the following to **scene_setup.py**:

```setup("name", "path to base scene", colliders)```

Here, the colliders are a function which creates Panda3D collision shapes. The ```setup``` function adds the scene to the **settings.py** list,
```scenes```. It also calls the function, ```create_models``` in **scene_setup.py**, where a list of Model objects (as seen above) are returned,
depending on which scene calls it.

### Creating cutscenes:
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
Note, that the player's p value can only be between -90 and 90.<br>
Cutscenes are normally created in **functions.py**, reffering to base.

### Converting .exr to .png:
I made a simple script which can convert .exr images to .png images. This is used when baking textures in Maya. The script is executed in the terminal. Use the following arguments for a description on how to use it:
```
exr2png.py -h
```
It has various keywords, which are explained there. An example of a conversion could look like this:
```
exr2png.py exr_folder png_folder 2 -o
```
Arguments are: input folder, output folder, exposure and overwrite files with the same names. If the input folder argument is omitted, the current directory will be used as input.<br>
**Note that this script required Numpy and OpenCV**
