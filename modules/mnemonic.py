import hashlib

from .entropy_generator import EntropyGenerator
from utils.config import BIP_39

class Mnemonic:
    def __init__(self, word_num: int, seed=None):
        if word_num == 12 or word_num == 24:
            self.word_num = word_num
            self.bit_length = int(word_num * 11 - word_num / 3)
            self.entropy_generator = EntropyGenerator(self.bit_length, seed)
        else:
            raise ValueError('The amount of words must be 12 or 24')
    
    def _to_sha256_hash(self, entropy: str) -> str:
        binary_data = int(entropy, 2).to_bytes((len(entropy) + 7) // 8, 'big')
        sha_256_hash_object = hashlib.sha256()
        sha_256_hash_object.update(binary_data)
        hashed_string = sha_256_hash_object.hexdigest()
        
        return hashed_string
    
    def _get_checksum(self, hashed_value: str) -> str:
        if self.word_num == 12:
            checksum = bin(int(hashed_value[0], 16))[2:].zfill(4)
        else:
            checksum = bin(int(hashed_value[:2], 16))[2:].zfill(8)
        
        return checksum
    
    def _divide_into_parts(self, bit_array: str, part_length=11) -> list[int]:
        key_array = [int(bit_array[i:i+part_length], 2) for i in range(0, len(bit_array), part_length)]
        
        return key_array
        
    def generate_mnemonic(self):
        entropy = self.entropy_generator.generate_entropy()
        hashed_string = self._to_sha256_hash(entropy)
        checksum = self._get_checksum(hashed_string)        
        bit_array = entropy + checksum
        
        num_array = self._divide_into_parts(bit_array)
        mnemonic = ' '.join(BIP_39[key] for key in num_array)
        
        return mnemonic
        
        
        
        