import json
import random
import time

f = open('user_agents.txt', 'r')
user_agents = json.load(f)


def get_ua():
    return random.choice(user_agents['browsers']['chrome'])


def get_proxy():
    pass


def sleep_random(start, end):
    time.sleep(random.uniform(start, end))
