def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


test_str = "Race car"
print(f"Is '{test_str}' a palindrome? {is_palindrome(test_str)}")
