import re

def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

if __name__ == "__main__":
    print(camel_to_snake("CamelCaseToSnakeCase"))