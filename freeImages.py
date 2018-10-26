import requests
import string
import random
import uuid
import time
import pickle

DELAY_TIME = 2.0
URL = "http://kunde.reedfoto.no/bestilling/thumb/"
STRING_SIZE = 8

def load():
    with open("pickle/freeImages_not_working.pkl", 'rb') as pkl:
        NOT_WORKING = pickle.load(pkl)
    with open("pickle/freeImages_working.pkl", 'rb') as pkl:
        WORKING = pickle.load(pkl)
    return WORKING, NOT_WORKING
    
def save(merged_working, not_working):
    with open("pickle/freeImages_not_working.pkl", 'wb') as pkl:
        pickle.dump(not_working, pkl)
    with open("pickle/freeImages_working.pkl", 'wb') as pkl:
        pickle.dump(merged_working, pkl)

def generate_random_string(base_string_character):
    ret_str = ''
    for i in range(STRING_SIZE):
        character = random.choice(base_string_character)
        ret_str += character
    return ret_str    

def testImage(repeat_times=100):
    WORKING, NOT_WORKING = load()
    WORKING_current = []
    repeat = repeat_times
    i = 0
    start = time.time()
    while i < repeat:
        i += 1
        works = False
        code = generate_random_string(string.digits + string.ascii_letters).upper()
        image_url = URL + code
        if code in NOT_WORKING or image_url in WORKING:
            print("Processing code: {} - {} out of {} - {}".format(code, i, repeat, "Dupe"), end='\r')
            repeat += 1
            continue
        response = requests.get(image_url).content
        if not "Fatal" in str(response):
            works = True
            WORKING_current.append(image_url)
        else:
            works = False
            NOT_WORKING.append(code)
        print("Processing code: {} - {} out of {} - {}".format(code, i, repeat, "Success" if works else "Failure"), end='\r')
        #time.sleep(DELAY_TIME * 0.5)
    end = time.time()
    print("Found {} valid images out of {} iterations - {:.3f}s".format(len(WORKING_current), i, end - start))
    merged_working = WORKING + WORKING_current
    save(merged_working, NOT_WORKING)
    return WORKING, NOT_WORKING

if __name__ is __name__:
    while True:
        try:
            WORKING, NOT_WORKING = testImage(200)
            print((
                "Current amount of codes that do not work: {}\n"
                "Current amount of codes that work: {}\n"
                "Estimated amount of codes left to process: {}\n"
                "---------------------------------------------------"
                ).format(
                    len(NOT_WORKING), 
                    len(WORKING), 
                    1000000 - (len(NOT_WORKING) + len(WORKING))
                )
            )
            time.sleep(DELAY_TIME)
        except ConnectionError:
            time.sleep(10000)