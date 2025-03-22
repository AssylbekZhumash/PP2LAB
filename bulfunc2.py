def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

input_str = "Hello World!"
upper, lower = count_case(input_str)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
