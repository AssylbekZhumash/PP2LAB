import re

def replace_with_colon(string):
    return re.sub(r'[ ,.]+', ':', string)

if __name__ == "__main__":
    print(replace_with_colon("Hello, world. How are you?"))