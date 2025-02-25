import re

def match_a_b(string):
    return bool(re.fullmatch(r'ab*', string))

if __name__ == "__main__":
    print(match_a_b("abb"))  
