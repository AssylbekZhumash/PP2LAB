import re

def find_upper_lower(string):
    return re.findall(r'[A-Z][a-z]+', string)

if __name__ == "__main__":
    print(find_upper_lower("HelloWorld ExampleText")) 
