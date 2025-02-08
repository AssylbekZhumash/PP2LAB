def is_palindrome(word):
    cleaned_word = word.replace(" ", "").lower()
    return cleaned_word == cleaned_word[::-1]