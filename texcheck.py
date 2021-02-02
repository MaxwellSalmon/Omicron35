import os, sys

args = sys.argv[1:]

#Be able to compare times for scene.
#Is one scene not having textures for one of the times?

def fetch_textures(scene):
    path_times = ['Day','Evening', 'Night']
    scene = format_scene(scene.lower())

    day_textures = []
    evening_textures = []
    night_textures = []
    
    try:
        for time in path_times:
            path = os.path.join('textures',time,scene)
            path = os.path.join(os.getcwd(), path)

            for file in os.listdir(path):
                #Skip files which are not png
                if not file.endswith('.png'):
                    continue
                if time == 'Day':
                    day_textures.append(file)
                elif time == 'Evening':
                    evening_textures.append(file)
                else:
                    night_textures.append(file)
    except Exception as e: 
        print("Oops, seems like there are some missing folders.")
        print(e)
        quit()
                
    return day_textures, evening_textures, night_textures


#This function converts shortcut names to real names
def format_scene(scene):
    if scene in ['house', 'interior', 'inte', 'int', 'i', 'houseinterior']:
        return 'HouseInterior'
    elif scene in ['outside', 'out', 'exterior', 'exte', 'ext', 'e', 'o']:
        return 'Exterior'
    elif scene in ['hangar', 'hang', 'hangarinterior', 'h']:
        return 'HangarInterior'
    else:
        print("Scene not recognized!")
        quit()

def compare_times(day, evening, night):
    unique_day = find_unique_tex(day, evening, night)
    unique_evening = find_unique_tex(evening, night, day)
    unique_night = find_unique_tex(night, day, evening)

    irregular_day = find_irregular_tex(day, evening, night)
    irregular_evening = find_irregular_tex(evening, night, day)
    irregular_night = find_irregular_tex(night,day, evening)

    i_d = [x for x in irregular_day if x not in unique_day]
    i_e = [x for x in irregular_evening if x not in unique_evening]
    i_n = [x for x in irregular_night if x not in unique_night]

    print_results(unique_day, unique_evening, unique_night,
                  i_d, i_e, i_n)
    

def find_irregular_tex(query, comp1, comp2):
    #Find textures, which are not in all times.
    irregularity = []

    for tex in query:
        #Skip textures which are found everywhere
        if tex in comp1 and tex in comp2:
            continue
        irregularity.append(tex)
        
    return irregularity

def find_unique_tex(query, comp1, comp2):
    #Find out which times lack a texture.
    unique = []

    for tex in query:
        if tex in comp1 or tex in comp2:
            continue
        unique.append(tex)

    return unique

def output(l):
    for i in l:
        print('\t',i)
    if len(l) == 0:
        print('\tNone')

def print_results(u_d, u_e, u_n, i_d, i_e, i_n):
    print("Textures not found in other scenes:")
    print('==================================')
    print("Unique day:")
    output(u_d)
    print("Unique evening:")
    output(u_e)
    print("Unique night:")
    output(u_n)
    print()
    print("Textures with mismatch:")
    print('==================================')
    print("Irregular day:")
    output(i_d)
    print("Irregular evening:")
    output(i_e)
    print("Irregular night:")
    output(i_n)
        
        

d,e,n = fetch_textures(args[0])
compare_times(d,e,n)
