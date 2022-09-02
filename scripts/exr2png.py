import numpy as np
import cv2
import sys, os

args = sys.argv[1:]
#arg1 = input folder
#arg3 = output folder
#arg3 = exposure

def convert(args, overwrite=False):
    lim = 65535
        
    if len(args) != 3:
        if not os.path.isdir(args[0]):
            print("Invalud arguments!")
            print("Syntax: exr2.png.py input_folder output_folder exposure")
            return
        else:
            args = [os.getcwd()] + args            

    try: 
        exp = 65535 * int(args[-1])
        for file in os.listdir(args[0]):
            #Don't convert files that are already in output folder
            if not overwrite and file[:-3] + 'png' in os.listdir(args[1]):
                continue
            if file.endswith(".exr"):
                print("Converting ", file)
                img = cv2.imread(os.path.join(args[0], file), -1)
                img = img * exp
                img[img>lim] = lim
                img = np.uint16(img)
                cv2.imwrite(os.path.join(args[1])+"\{}.png".format(file[:-4]), img)
        print("Done! Have a nice day :-)")
    except Exception as e:
        print("Invalud arguments!")
        print("Syntax: exr2.png.py input_folder output_folder exposure")
        print()
        print(e)

def view(args):
    lim = 65535
    exp = 65535 * int(args[-1])
    if not os.path.isdir(args[0]):
        path = os.getcwd()
    else:
        path = args[0]
        
    for file in os.listdir(path):
        if file.endswith(".exr"):
            img = cv2.imread(os.path.join(path, file), -1)
            img = img * exp
            img[img>lim] = lim
            img = np.uint16(img)
            cv2.imshow("Press ESC or Q to quit", img)
            k = cv2.waitKey(0)
            if k == 27 or k == 113:
                break
            
if [x for x in ['h', '-h', 'help', '?'] if x in args] or not args:
   print("This script converts .exr images to .png images.")
   print()
   print("Syntax:")
   print('"exr2png.py input_folder output_folder exposure"')
   print('"exr2png.py output_folder exposure"')
   print()
   print("Additional keywords:")
   print("-h : help page")
   print("-v : view images instead of converting")
   print("-o : overwrite images in output folder")
   print("")
   print("When viewing images:")
   print("Press ESC or Q to stop viewing")
   print("Press any other key to view next image")
elif args[-1] == '-o' or args[-1] == 'o':
    convert(args[:-1], True)
elif args[-1] != '-v' and args[-1] != 'v':
    convert(args)
else:
    view(args[:-1])
