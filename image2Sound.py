import numpy
import pyaudio
import math
import argparse
import time
from PIL import Image, ImageFilter
 
class ToneGenerator(object):
 
    def __init__(self, samplerate=44100, frames_per_buffer=4410):
        self.p = pyaudio.PyAudio()
        self.samplerate = samplerate
        self.frames_per_buffer = frames_per_buffer
        self.streamOpen = False
 
    def sinewave(self):
        if self.buffer_offset + self.frames_per_buffer - 1 > self.x_max:
            # We don't need a full buffer or audio so pad the end with 0's
            xs = numpy.arange(self.buffer_offset,
                              self.x_max)
            tmp = self.amplitude * numpy.sin(xs * self.omega)
            out = numpy.append(tmp,
                               numpy.zeros(self.frames_per_buffer - len(tmp)))
        else:
            xs = numpy.arange(self.buffer_offset,
                              self.buffer_offset + self.frames_per_buffer)
            out = self.amplitude * numpy.sin(xs * self.omega)
        self.buffer_offset += self.frames_per_buffer
        return out
 
    def callback(self, in_data, frame_count, time_info, status):
        if self.buffer_offset < self.x_max:
            data = self.sinewave().astype(numpy.float32)
            return (data.tostring(), pyaudio.paContinue)
        else:
            return (None, pyaudio.paComplete)
 
    def is_playing(self):
        if self.stream.is_active():
            return True
        else:
            if self.streamOpen:
                self.stream.stop_stream()
                self.stream.close()
                self.streamOpen = False
            return False
 
    def play(self, frequency, duration, amplitude):
        self.omega = float(frequency) * (math.pi * 2) / self.samplerate
        self.amplitude = amplitude
        self.buffer_offset = 0
        self.streamOpen = True
        self.x_max = math.ceil(self.samplerate * duration) - 1
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.samplerate,
                                  output=True,
                                  frames_per_buffer=self.frames_per_buffer,
                                  stream_callback=self.callback)


parser = argparse.ArgumentParser()
parser.add_argument('-i', type=str, help="Image to play", dest="image", required=True)
parser.add_argument('-s', action='store_true', help="Save blurred image", dest="save_blurred")
args = parser.parse_args()

tone_generator = ToneGenerator(frames_per_buffer=1200)

IMAGE_SIZE = 64, 64
MIN_FREQUENCY = 100
MAX_FREQUENCY = 16000
MIN_DURATION = 0.1
MAX_DURATION = 0.5
MIN_AMPLITUDE = 0.5
MAX_AMPLITUDE = 1
BLUR_VALUE = 0.075

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def play_pixels(image_path, save_blurred=False):
    #Open image fro the path provided
    im = Image.open(image_path)
    # Apply a gaussian blur to the image
    im = im.filter(ImageFilter.GaussianBlur(radius=im.size[1] * BLUR_VALUE))
    # Resize the image while keeping the aspect ratio
    im.thumbnail(IMAGE_SIZE)
    
    # If save_blurred is true then save the new blurred image
    if save_blurred:
        im.save("out.jpg", "JPEG")
    
    # Load the pixels into a two-dimentional array
    pixels = im.load()
    
    start = time.time()
    # Loop over all the pixels
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            _frequency = translate(pixels[i,j][0], 0, 255, MIN_FREQUENCY, MAX_FREQUENCY)
            _duration = translate(pixels[i,j][1], 0, 255, MIN_DURATION, MAX_DURATION)
            _amplitude = translate(pixels[i,j][2], 0, 255, MIN_AMPLITUDE, MAX_AMPLITUDE)
            tone_generator.play(_frequency, _duration, _amplitude)
            while tone_generator.is_playing():
                pass
            print(f"Playing note {i+j} out of {im.size[0] * im.size[1]}", end='\r')
            
    print(f"Took {time.time() - start} to loop over all pixels")
    # Close the image
    im.close()
    
    return
    
if __name__ == "__main__":
    play_pixels(args.image, save_blurred=args.save_blurred)
