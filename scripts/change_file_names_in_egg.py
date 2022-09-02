import os

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

def change_textures(path, replace, walk=False):
    models = find_files(path, walk)

    print(f"You are about to change the contents of {len(models)} file(s).")
    print(f"A backup of the folder \"{path}\" is recommended.")
    print("Are you sure you want to do this?")
    yn = input('Y/N > ')
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
    
