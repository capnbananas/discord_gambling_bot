from PIL import Image, ImageDraw, ImageFont, ImageSequence
import imageio
import os

#----------------------------------------------------------------------------------------------------
size = 400, 400
new_path = 'games/images/newimg/'
im = Image.open("games/images/slot.gif")
image_folder = os.fsencode(new_path)

def thumbnails(frames):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.ANTIALIAS)
        yield thumbnail

def img_ready():
	filenames  = []

	for file in os.listdir(image_folder):

	    filename = os.fsdecode(file)

	    if filename.endswith(('.png')):

	        filenames.append(new_path + filename)

	filenames.append('games/images/slot_output.png')
	images = list(map(lambda filename: imageio.imread(filename), filenames))
	imageio.mimsave(os.path.join('games/images/slot.gif'), images, duration = 0.02, loop=1)
	frames = ImageSequence.Iterator(im)
	frames = thumbnails(frames)
	om = next(frames)
	om.info = im.info
	om.save("games/images/out.gif", save_all=True, append_images=list(frames))


#----------------------------------------------------------------------------------------------------
