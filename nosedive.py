import numpy as np
import random
import requests


def debug_random_profile_generator(final_rank, rating_amount, username=None, description=None, variation=5):
    '''Generates a random profile'''
    profile = {}
    
    # Generate a random username and put it into the profile dictionary
    if not username:
        username = requests.get(url='https://randomuser.me/api/').json()['results'][0]['name']['first']
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
        'rank': rank
    }
    profile_to_rank = calculate_rating(rank, profile_to_rank)
    
    return profile_to_rank


if __name__ == "__main__":
    my_profile = debug_random_profile_generator(3.156, 50, username='Tymec', description=';/', variation=5)
    print(f'{my_profile["username"]}: {my_profile["rank"]}')
    another_profile = debug_random_profile_generator(4.755, 500, variation=5)
    print(f'{another_profile["username"]}: {another_profile["rank"]}')
    my_profile = rank(another_profile, my_profile, 5.0)
    print(f'{my_profile["username"]}: {my_profile["rank"]}')
