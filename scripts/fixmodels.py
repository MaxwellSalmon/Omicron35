import os, sys

args = sys.argv[1:]

def find_files(path, walk):
    '''path - folder to search
       replace - tuple (search, replace)
       walk - search sub folders?'''
    
    files = os.listdir(path)
    models = []
    
    for file in files:
        if file[-3:] == 'egg':
            models.append(path+'/'+file)
        elif '.' not in file:
            if walk:
                sub_models = find_files(path+'/'+file, walk)
                for i in sub_models:
                    models.append(i)
                    
    return models

def auto_replace():
    return ("""../../../Portfolio/Panda3D/Omicron 35/textures""", """../textures""")

def show_example(models, replace):
    for egg in models:
        file = open(egg, 'r')
        old_string = file.read()
        new_string = old_string.replace(replace[0], replace[1])
        file.close()
    
        index1 = old_string.find(replace[0])
        if index1 == -1:
            continue
        index1_end = old_string[index1:index1+100].find('\n')

        index2 = new_string.find(replace[1])
        if index2 == -1:
            continue
        index2_end = new_string[index2:index2+100].find('\n')
        
        print(f"""\"{old_string[index1:index1+index1_end-1]}" --> "{new_string[index2:index2+index2_end-1]}\"""")
        print("Do you want to replace?")
        return
    print("Found no models with specified replace string")
    

def run(path='../models', replace=None, walk=True, output=True):
    print(path, replace, walk)
    models = find_files(path, walk)

    if not replace:
        print("!! No replace string specified. Using default string !!")
        replace = auto_replace()
        print()

    if output:
        print(f"You are about to change the contents of {len(models)} file(s).")
        print(f"A backup of the folder \"{path}\" is recommended.")
        print("type \"f\" to see an example of a changed path.")
        print("Are you sure you want to do this?")
    yn = input('Y/N > ')
    if yn.lower() in ['f', 'file', 'files']:
        print()
        show_example(models, replace)
        run(path, replace, walk, output=False)
        return
    if yn.lower() not in ['y', 'yes']:
        print("Understandable.")
        return
    print("Alright! Let's do this.")

    for egg in models:
        file = open(egg, 'r')
        string = file.read()
        string = string.replace(replace[0], replace[1])
        file.close()

        file = open(egg, 'w')
        file.write(string)        
        file.close()

    print("Done!")

if [x for x in ['h', '-h', 'help', '?'] if x in args] or not args:
   print("This script changes texture paths to be relative.")
   print()
   print("Syntax:")
   print('"fixmodels.py run path replace walk"')
   print()
   print("Path is path to folder, where models are located. Default is ../models")
   print("Replace arg is a tuple of strings (search, replace). Has default.")
   print("Walk arg is bool, determining whether to walk subfolders. Default is True")
   print("All arguments are keywords.")
   print()
   print("Example:")
   print("fixmodels.py run path=../../models replace=(../../project/textures,../textures) walk=False")
   print()
   print("Additional keywords:")
   print("-h : this help page")
elif args[0].lower() == 'run':
    print(args)
    run(**dict(arg.split('=') for arg in args[1:])) # kwargs
