import re

def insert_spaces_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

if __name__ == "__main__":
    print(insert_spaces_capitals("InsertSpacesBetweenWords"))