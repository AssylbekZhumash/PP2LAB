def tuple_all_true(t):
    return all(t)

test_tuple = (True, 1, "non-empty", [1,2,3])
print("All elements in", test_tuple, "are true:", tuple_all_true(test_tuple))

test_tuple2 = (True, 0, "hello")
print("All elements in", test_tuple2, "are true:", tuple_all_true(test_tuple2))
