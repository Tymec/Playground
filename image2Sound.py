import argparse
import pyaudio
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, help="Image", dest="image", required=True)
args = parser.parse_args()

im = Image.open(args.image)
pixels = im.load()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        print(pixels[i,j])

