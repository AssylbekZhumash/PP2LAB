import re

def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

if __name__ == "__main__":
    print(snake_to_camel("hello_world_example"))