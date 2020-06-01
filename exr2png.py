import numpy as np
import cv2
import sys, os

args = sys.argv[1:]
#arg1 = input folder
#arg3 = output folder
#arg3 = exposure

def convert(args):
    lim = 65535
    if len(args) != 3:
        print("Invalud arguments!")
        print("Syntax: exr2.png.py input_folder output_folder exposure")
        return

    try: 
        exp = 65535 * int(args[-1])
        for file in os.listdir(args[0]):
            print("Converting ", file)
            if file.endswith(".exr"):
                img = cv2.imread(os.path.join(args[0], file), -1)
                img = img * exp
                img[img>lim] = lim
                img = np.uint16(img)
                cv2.imwrite(os.path.join(args[1])+"\{}.png".format(file[:-4]), img)
        print("Done! Have a nice day :-)")
    except Exception as e:
        print(e)

def view(args):
    lim = 65535
    exp = 65535 * int(args[-1])
    for file in os.listdir(args[1]):
        if file.endswith(".exr"):
            img = cv2.imread(os.path.join(args[1], file), -1)
            img = img * exp
            img[img>lim] = lim
            img = np.uint16(img)
            cv2.imshow("Press ESC or Q to quit", img)
            k = cv2.waitKey(0)
            if k == 27 or k == 113:
                break
                   
            
    

if args[0] != '-v' and args[0] != 'v':     
    convert(args)
else:
    view(args)


