import sys
import questionary

from questionary import Choice
from typing import List

from modules import Mnemonic
from utils import center_output, format_input


def get_word_number():
    result = questionary.select(
        "Select number of words to create mnemonic",
        choices=[
            Choice("1) 12 words", 12),
            Choice("2) 24 words", 24)
        ],
        qmark="| ⚙️ ",
        pointer="✅ "
    ).ask()
    
    return result


def greetings():
    brand_label = "========== M A K E D 0 N 1 A N =========="
    name_label = "========= Wallet Creator ========="
    
    print("")
    center_output(brand_label)
    center_output(name_label)
    
    
def create_wallets() -> List[str]:    
    number_of_words = get_word_number()
    wallet_number = int(format_input("How much wallets do you want?"))
    
    center_output("Do you want to use seed for more randomness?")
    is_seed = format_input("Type '1' if you want, '0' if not: ")
    
    mnemonics: List[str] = []
    
    if is_seed == '1':
        seed = format_input("Enter your any seed (it can by any number or string): ")
        mnemonic = Mnemonic(number_of_words, seed)
    elif is_seed == '0':
        mnemonic = Mnemonic(number_of_words)
    else:
        center_output("Incorrect input! Exiting...")
        sys.exit()
    
    for _ in range(wallet_number):        
        mnemonics.append(mnemonic.generate_mnemonic())
    
    return mnemonics
        
        
def write_to_txt(mnemonics: List[str]):
    with open('wallets.txt', 'w') as file:
        file.write('\n'.join(mnemonics))            


def main():
    greetings()    
    mnemonics = create_wallets()
    write_to_txt(mnemonics)
    center_output('The mnemonics has been created successfully!')


if __name__ == '__main__':
    main()