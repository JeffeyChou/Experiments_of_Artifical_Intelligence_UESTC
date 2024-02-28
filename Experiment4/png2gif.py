# read pngs files and convert them to one gif

import os
import imageio


def png2gif(png_dir, gif_name):
    png_files = os.listdir(png_dir)
    png_files.sort()
    print(png_files)
    png_files = [os.path.join(png_dir, f) for f in png_files]
    frames = []
    for image_name in png_files:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.2)

if __name__ == '__main__':
    png_dir = 'pngs'
    gif_name = 'test.gif'
    png2gif(png_dir, gif_name)

