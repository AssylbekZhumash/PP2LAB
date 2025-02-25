import re

def match_a_any_b(string):
    return bool(re.fullmatch(r'a.*b', string))

if __name__ == "__main__":
    print(match_a_any_b("axxxb"))  