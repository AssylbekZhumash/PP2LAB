from grams_to_ounces import grams_to_ounces
from fahrenheit_to_centigrade import fahrenheit_to_centigrade
from solve_puzzle import solve
from filter_prime import filter_prime
from string_permutations import string_permutations
from reverse_words import reverse_words
from has_33 import has_33
from spy_game import spy_game
from sphere_volume import sphere_volume
from unique_elements import unique_elements
from is_palindrome import is_palindrome
from histogram import histogram


def test_imported_functions():
    print("Converting 100 grams to ounces:", grams_to_ounces(100))
    print("Fahrenheit to Centigrade for 98.6°F:", fahrenheit_to_centigrade(98.6))
    print("Chicken and Rabbit puzzle for 35 heads, 94 legs:", solve(35, 94))
    print("Prime filter for [2, 4, 5, 6, 9, 11]:", filter_prime([2, 4, 5, 6, 9, 11]))
    print("Permutations of 'abc':", string_permutations('abc'))
    print("Reversing words of 'We are ready':", reverse_words('We are ready'))
    print("Check has_33 for [1, 3, 3]:", has_33([1, 3, 3]))
    print("Spy game for [1, 2, 4, 0, 0, 7, 5]:", spy_game([1, 2, 4, 0, 0, 7, 5]))
    print("Sphere volume for radius 5:", sphere_volume(5))
    print("Unique elements in [1, 2, 2, 3, 4, 4, 5]:", unique_elements([1, 2, 2, 3, 4, 4, 5]))
    print("Is 'madam' a palindrome?:", is_palindrome("madam"))
    print("Histogram for [4, 9, 7]:")
    histogram([4, 9, 7])

# Uncomment to run the guess the number game
# from guess_the_number import guess_the_number
# guess_the_number()

# Run test functions
test_imported_functions()