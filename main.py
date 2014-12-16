import string
import random
import json
from collections import defaultdict

def make_hash_from_json(filename, default=None):
    if not default:
        to_load = dict()
    else:
        to_load = defaultdict(default)
    with open(filename) as f:
        original_json = json.load(f)
    for k,v in original_json:
        to_load[k] = v
    return to_load

url_hash = make_hash_from_json('url_hash.json')
count_hash = make_hash_from_json('count_hash.json', default=0)

def save_hash_to_json(filename, to_dump):
    with open(filename, 'w') as f:
        json.dump(to_dump, f)

def generate_shortened_url():
    pool = list(string.digits) + list(string.letters)
    return ''.join(random.choice(pool) for _ in range(6))

def add_shortened_url(url):
    global url_hash
    new_short_url = generate_shortened_url()
    while new_short_url in url_hash:
        new_short_url = generate_shortened_url()
    url_hash[new_short_url] = url
    save_hash_to_json('url_hash.json', url_hash)
    return new_short_url

def increment_counts(short_url):
    global count_hash
    count_hash[short_url] += 1
    save_hash_to_json('count_has.json', count_hash)