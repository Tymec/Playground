import requests
import string
import random
import uuid
import time
import pickle

DELAY_TIME = 0.5
URL = "http://kunde.reedfoto.no/bestilling/thumb/"
STRING_SIZE = 8
NOT_WORKING = []
RESULT = []

def load():
    global NOT_WORKING
    with open("pickle/freeImages_not_working.pkl", 'rb') as pkl:
        NOT_WORKING = pickle.load(pkl)
    
def save(result_current):
    global RESULT
    RESULT += result_current
    with open("pickle/freeImages_not_working.pkl", 'wb') as pkl:
        pickle.dump(NOT_WORKING, pkl)
    with open("pickle/freeImages_result.pkl", 'wb') as pkl:
        pickle.dump(RESULT, pkl)

def generate_random_string(base_string_character):
    ret_str = ''
    for i in range(STRING_SIZE):
        character = random.choice(base_string_character)
        ret_str += character
    return ret_str    

def testImage(repeat_times=50):
    load()
    result_current = []
    repeat = repeat_times
    for i in range(repeat):
        works = False
        code = generate_random_string(string.digits + string.ascii_letters).upper()
        if code in NOT_WORKING:
            repeat += 1
            continue
        image_url = URL + code
        response = requests.get(image_url).content
        if not "Fatal" in str(response):
            works = True
            result_current.append(image_url)
        else:
            works = False
            NOT_WORKING.append(code)
        print("Processing code: {} - {} out of {} - {}.".format(code, i, repeat, "Succeeded" if works else "Failed"))
        #time.sleep(DELAY_TIME)
    print("Found {} valid images out of {}.".format(len(result_current), repeat))
    save(result_current)

if __name__ is __name__:
    testImage(100)