# Omicron35
A work in progress Panda3D game by MaxwellSalmon.
[![What it looks like so far](https://i.imgur.com/KR57VyA.png)](https://www.youtube.com/watch?v=5HnweyMsE24)

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
ambience = string
stop_ambience_on = ['bools']
```
The keyword, ```name``` is only necessary, for interactive models, if there are multiple objects sharing the same 3D-model.<br>
Models are created in the script **scene_setup.py**

An example for loading an interactive model, which changes the scene can be seen here:
```
Model('door', name='ext_door', tag='interactive', pos=(14,1.35,0.4), scale=0.5, solid=True, culling='both'
                        function=[functions.change_scene, {'to_scene':'inte_d1_t1'}])
```

### Changing scene function:
The function  ```functions.change_scene``` can be applied to a model - a door in most cases. This function will fade between scenes and load new textures or days. The function takes a dictionary of kwargs:

```
to_scene = 'scene_name'
bools = ['bool1', 'bool2']
voices = ['audio1', 'audio2']
bool = 'bool'
voice = 'audio'
```

```bools``` can be used, if multiple bools need to be true in order for the scene to change. The bools are the same strings found in ```settings.g_bools```. Add a '!' as the first char in the string if the bool should be False.
```voices``` is a list of ```voice_string``` names, which should be played if a bool is not fulfilled. The indecies tie the voices to the bools. 
If only one bool is required, you can do the same in ```bool``` and ```voice```, so you don't need the brackets.

### Creating scenes:
A scene consists of base elements and scene-specific elements. The base elements are the scene model and its colliders. To create a scene, add the following to **scene_setup.py**:

```setup("name", "path to base scene", colliders)```

Here, the colliders are a function which creates Panda3D collision shapes. The ```setup``` function adds the scene to the **settings.py** list,
```scenes```. It also calls the function, ```create_models``` in **scene_setup.py**, where a list of Model objects (as seen above) are returned,
depending on which scene calls it.

### Creating cutscenes:
```
base.cutscene([{point},{point}, ..., {point}])
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

### Creating conversations and voices:
In **voice_strings.py** you can create voice clips. You need to provide subtitles using the file name as key. In the dictionaru `conversations`, you will find sequences of speech, making up conversations between the player and HQ. Does the name start with ```hq_```, the voice will belong to the radio.
To create a conversation with buttons for speech selection, edit **conversation_flow.py**. Here, you create conversation states.
A conversation state consists of speech followed by buttons. Each button has a transition to another state.
The arguments taken by a conversation state is the following:
```
name = string
audio_sequence = string (key from voice_strings.py)
button_strings = [strings shown on buttons]
transitions = [strings with state names]
end_state = bool
```
If `end_state` is true (false by default), no buttons will be shown and the player will stop the conversation. However, it still needs one transition, which will be the state when the player talks the next day.
Below is an example of the state `day1` transitioning to two other states. 

```
CS('day1', 'radio_day1', ['What! Again?', 'bruh.'], ['day1_what_again', 'bruh']),
CS('day1_what_again', 'radio_day1_2', None, 'day2', end_state=True),
CS('bruh', 'radio_day1_3', None, 'day2', end_state=True),
```

### Creating triggers:
```
Trigger(x, y, z, radius, function, **kwargs)
```
Similar to models, this is loaded in **scene_setup.py** and should be in a list for scenes. Possible kwargs are:
```
mode = string
name = string
```
`mode` can be either `enter`, `enter_once` or `enterleave` right now, controlling when the function should be called. `name` is just to easier refer to the trigger in case of an error.
All triggers are spheres and will be visible if `show_cols` in **settings.py** is enabled.

# Developer tools

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

### Checking inconsistencies in textures
I also made a simple CLI for getting an overview in textures. From the command prompt, call the following:
```
texcheck.py <interior/exterior/hangar>
```
This will show the different times for a scene with unique textures, missing textures and general texture irregularities. The argument for the scene has some shortcuts, like `i`, `e` and `h`.

### Editing texture file paths'
When I push changes, the file paths for model textures are most likely not relative, causing issues for other users. If this occurs, refer to the script ```fixmodels``` in the scripts folder. Here, you can change file paths in all models at once. In the command prompt, type ```fixmodels.py``` for more information.

### The developer console
Press 'f1' to open the developer console. While in here, type '?' and enter to see a list of commands. To see the usage of a command, type '? command'.
To add a new command, go to `commands.py` and write your function, which needs to return a string. In The two dictionaries, you write which keyword should trigger each warning and the help string for the command.


### License
This project is under GNU GPLv3 licence.
If you disagree with this choice, feel free to contact me.
