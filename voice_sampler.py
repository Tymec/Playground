import sounddevice as sd
from scipy.io.wavfile import write
import csv
import time

sentence_list = []
with open('text.txt', 'r') as f:
  for line in f:
    sentence_list.append(line)

sample_rate = 44100
seconds = 10
id_prefix = "LJ-"

with open('transcript.csv', 'w') as f:
  writer = csv.writer(f, delimiter='|')
  for i, sentence in enumerate(sentence_list):
    id = id_prefix + '{:03}'.format(i)
    writer.writerow([id, sentence])
    print(sentence)

    recording = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    write(id + '', samplerate, recording)
    time.sleep(3)
