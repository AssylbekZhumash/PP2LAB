import re

def match_a_bbb(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

if __name__ == "__main__":
    print(match_a_bbb("abb"))  