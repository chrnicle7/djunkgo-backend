import random
import string

class RandomStringHelper():

    @staticmethod
    def generate_random_str():
        letters = string.ascii_letters

        return ''.join(random.choice(letters) for i in range(32))