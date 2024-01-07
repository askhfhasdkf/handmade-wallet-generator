import json

from pathlib import Path


def center_output(message: str):
    print(f"| {message:^59}|")
    
    
def format_input(message: str) -> str:
    print(f"| {message:^59}|", end='\n| ', flush=True)    
    value = input()
    
    return value


def load_json(filepath: Path | str):
    with open(filepath, 'r') as file:
        return json.load(file)