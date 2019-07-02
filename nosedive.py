import numpy as np
import random
import requests
import time


def create_profile(information):
    '''Creates a profile'''
    # Simple schema of the profile dictionary
    profile = {
        'data': {
            'id': information['data']['id'],
            'username': information['data']['username'],
            'bio': information['data']['bio'],
            'status': information['data']['status']
        },
        'rank': {
            'current_rank': information['rank']['current_rank'],
            'previous_ranks': [
                information['rank']['previous_ranks'][0],
                information['rank']['previous_ranks'][1],
                information['rank']['previous_ranks'][2]
            ]
        },
        'personal': {
            'name': {
                'first_name': information['personal']['name']['first_name'],
                'middle_name': information['personal']['name']['middle_name'],
                'last_name': information['personal']['name']['last_name']
            },
            'information': {
                'birthday': information['personal']['information']['age'],
                'gender': information['personal']['information']['gender'],
                'height': information['personal']['information']['height'],
                'weight': information['personal']['information']['weight'],
                'relationship_status': information['personal']['information']['relationship_status'],
            },
            'contact': {
                'phone_number': information['personal']['contact']['phone_number'],
                'email': information['personal']['contact']['email']
                'social_media': {
                    'facebook': information['personal']['contact']['social_media']['facebook'],
                    'snapchat': information['personal']['contact']['social_media']['snapchat'],
                    'instagram': information['personal']['contact']['social_media']['instagram']
                }
            },
            'address': {
                'country': information['personal']['address']['country']
                'city': information['personal']['address']['city'],
                'zip_code': information['personal']['address']['zip_code'],
                'street': information['personal']['address']['street'],
            }
        },
        'images': {
            'profile': information['images']['profile'],
            'album': {
                'image1': {
                    'original': information['images']['album']['image1']['original'],
                    'thumbnail': information['images']['album']['image1']['thumbnail'],
                    'resized': {
                        'small': information['images']['album']['image1']['resized']['small'],
                        'medium': information['images']['album']['image1']['resized']['medium'],
                        'large': information['images']['album']['image1']['resized']['large']
                    }
                },
                'image2': {
                    'original': information['images']['album']['image2']['original'],
                    'thumbnail': information['images']['album']['image2']['thumbnail'],
                    'resized': {
                        'small': information['images']['album']['image2']['resized']['small'],
                        'medium': information['images']['album']['image2']['resized']['medium'],
                        'large': information['images']['album']['image2']['resized']['large']
                    }
                },
                'image3': {
                    'original': information['images']['album']['image3']['original'],
                    'thumbnail': information['images']['album']['image3']['thumbnail'],
                    'resized': {
                        'small': information['images']['album']['image3']['resized']['small'],
                        'medium': information['images']['album']['image3']['resized']['medium'],
                        'large': information['images']['album']['image3']['resized']['large']
                    }
                }
            }
        },
        'devices': {
            'SM-G950FD': {
                'hwid': information['devices']['SM-G950FD']['hwid'],
                'date_added': information['devices']['SM-G950FD']['date_added'],
                'os': information['devices']['SM-G950FD']['os'],
                'ip': information['devices']['SM-G950FD']['ip']
            },
            'SM-455GFD': {
                'hwid': information['devices']['SM-455GFD']['hwid'],
                'date_added': information['devices']['SM-455GFD']['date_added'],
                'os': information['devices']['SM-455GFD']['os'],
                'ip': information['devices']['SM-455GFD']['ip']
            }
        },
        'private': {
            'tracking': {
                'tracking_id': information['private']['tracking']['tracking_id']
            },
            'billing': {
                'paypal': {
                    'hashed': {
                        'email': information['private']['billing']['paypal']['email'],
                        'pasword': information['private']['billing']['paypal']['pasword']
                    }
                },
                'credit_card': {
                    'hashed': {
                        'number': information['private']['billing']['paypal']['number'],
                        'cvv': information['private']['billing']['paypal']['cvv'],
                        'expiration_date': {
                            'expiration_month': information['private']['billing']['paypal']['expiration_date']['expiration_month'],
                            'expiration_year': information['private']['billing']['paypal']['expiration_date']['expiration_year']
                        },
                        'name': {
                            'first_name': information['private']['billing']['paypal']['name']['first_name'],
                            'last_name': information['private']['billing']['paypal']['name']['last_name']
                        }
                    }
                }
            }
        }
    }
    return profile


def debug_random_profile_generator(final_rank, rating_amount, username=None, description=None, variation=5):
    '''Generates a random profile'''
    profile = {}
    
    # Generate a random username and put it into the profile dictionary
    if not username:
        username = requests.get(url='https://randomuser.me/api/').json()['results'][0]['name']['first'].title()
    profile['username'] = username
    
    if description:
        profile['description'] = description
    profile['description'] = f'Hello! My name is {username}.'
    
    # Generates a rank list and a final rank
    profile['rank_list'] = np.zeros(rating_amount, dtype=np.float32)
    profile['rank_list'][0] = random.uniform(0.0, 5.0)
    for i in range(1, rating_amount + 1):
        required_rank = final_rank * (i + 1) - np.sum(profile['rank_list'])
        if random.randint(0, variation) == 5:
            required_rank = random.uniform(0.0, 5.0)
        profile['rank_list'][i - 1] = np.clip(required_rank, 0.0, 5.0)
    profile['rank'] = np.mean(profile['rank_list'])
    return profile


def calculate_rating(rank, profile):
    '''Calculates the rating based on your previous ranks'''   
    profile['rank_list'] = np.append(profile['rank_list'], rank['rank'])
    profile['rank'] = np.mean(profile['rank_list'])
    return profile


def rank(profile, profile_to_rank, rank):
    '''Give a rank to someone'''
    rank = {
        'profile': profile,
        'rank': rank + profile['rank']
    }
    new_profile = calculate_rating(rank, profile_to_rank)
    return new_profile


if __name__ == "__main__":
    time_start = time.time()
    
    my_profile = debug_random_profile_generator(3.156, 50, username='Tymec', description=';/', variation=5)
    print(f'{my_profile["username"]}: {my_profile["rank"]} | {time.time() - time_start}ms')
    
    time_start = time.time()
    another_profile = debug_random_profile_generator(4.755, 500, variation=5)
    print(f'{another_profile["username"]}: {another_profile["rank"]} | {time.time() - time_start}ms')
    
    time_start = time.time()
    my_profile = rank(another_profile, my_profile, 5.0)
    print(f'{my_profile["username"]}: {my_profile["rank"]} | {time.time() - time_start}ms')
