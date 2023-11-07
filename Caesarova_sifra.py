import string
import unicodedata
from sys import stdout
from os import path
import click


alphabet = string.ascii_uppercase
stdout.write(path.dirname(__file__))
adr = path.dirname(__file__)

@click.command()
@click.option("-i", "--input", default="-", help="Is used for a word or sentence to cypher/decypher")
@click.option("-s", "--shift", default=1, help="Set up for how many letters it should shift")
@click.option("-d", "--decypher", default=False, help="Is used for decyphering")
@click.argument("output", default=stdout, type=click.File('w'), required=True)

def command_handle(input, shift, decypher, output):
    if decypher == True:
        print("run")
        result = decode(input, shift)
    else:
        result = cypher(input, shift)
    
    if output == stdout:
        print("\n" + result)
    else:
        output.write(result)
        

def cypher(text: str, key:int):
    text = text.upper()
    result = ""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    for char in text:
        if char >= "A" and char <= "Z":
            position = ord(char) - 65
            new_position = (position + key) % 26
            result += chr(new_position+65)
        else:
            continue       
    return(result) 


def decode(text: str, key:int):
    text = text.upper()
    result = ""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    for char in text:
        if char >= "A" and char <= "Z":
            position = ord(char) - 65
            new_position = (position - key) % 26
            result += chr(new_position+65)
        else:
            continue        
    return(result) 


if __name__ == '__main__':
    command_handle()
