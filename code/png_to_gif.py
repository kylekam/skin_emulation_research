from PIL import Image
import glob

# Sort by png number
def imgNum(file):
    return int(file[file.rindex('/')+1:file.rindex('.')])

# Create the frames 
frames = []
imgs = glob.glob("./weight/eval/michelle/cross_jumps/*.png")

imgs.sort(key=imgNum)

for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('test2_crossjumps.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=33, loop=0)