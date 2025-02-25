import re

def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

if __name__ == "__main__":
    print(split_at_uppercase("SplitAtUppercase"))