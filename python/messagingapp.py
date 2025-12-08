import random
import math

class user():
    def __init__(self, username, password):
        self.username = username
        self.passwords = password
        message_history = []

user1 = user('Maurice', 'Cuchibambo')

block_size = 3

def CBCencryption(text_to_encrypt:str,key:int,vi) -> str:
    text_to_encrypt = text_to_encrypt.strip()

splitString('hello')

def toBinary(a:str):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m