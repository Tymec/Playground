import requests
import string
import random
import uuid
import time
import pickle
import json

DELAY_TIME = 2.0
STRING_SIZE = 8
POSSIBILITIES = pow(26 + 10, STRING_SIZE)     #COUNT OF ALPHABET AND NUMBERS TO THE POWER OF STRING_SIZE
URL = "http://kunde.reedfoto.no/bestilling/thumb/"
PROXY = {
    "https": "https://190.145.140.174:51010"
}


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
    with open("pickle/freeImages_url.json", 'w') as f:
        json.dump(merged_working, f, indent=4)

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
            
        response = requests.get(image_url, proxies=PROXY).content
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
    return WORKING, NOT_WORKING, (end - start)

if __name__ is __name__:
    while True:
        try:
            WORKING, NOT_WORKING, TIME = testImage(200)
            print((
                "Current amount of codes that do not work: {}\n"
                "Current amount of codes that work: {}\n"
                "Estimated amount of codes left to process: {}\n"
                "Estimated time left: {:.0f}h\n"
                "---------------------------------------------------"
                ).format(
                    len(NOT_WORKING), 
                    len(WORKING), 
                    POSSIBILITIES - (len(NOT_WORKING) + len(WORKING)),
                    (round((POSSIBILITIES - (len(NOT_WORKING) + len(WORKING)))/200) * TIME)/pow(60, 2)
                )
            )
            time.sleep(DELAY_TIME)
        except requests.ConnectionError:
            print("\nWaiting for 10000s\n")
            time.sleep(10000)