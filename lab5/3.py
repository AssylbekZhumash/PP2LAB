import re

def find_lower_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

if __name__ == "__main__":
    print(find_lower_underscore("hello_world test_example")) 