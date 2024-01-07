import random


class EntropyGenerator():
    def __init__(self, bit_length: int = 128, seed = None):
        self.bit_length = bit_length
        if seed is not None:
            random.seed(seed)
            
    def generate(self) -> str:
        '''
        Returns string of 128 or 256 bits
        '''
        bit_string = bin(random.getrandbits(self.bit_length))[2:].zfill(self.bit_length)
        
        return bit_string
        