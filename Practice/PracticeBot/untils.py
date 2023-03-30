import hashlib
import time
import re

def generate_token():
    return hashlib.md5(str(time.time()).encode()).hexdigest().upper()*3


def encode_password(password:str): 
    return hashlib.md5(password.encode()).hexdigest()
    
