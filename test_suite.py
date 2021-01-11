def test_list_is_palindromic(arr: list) -> bool:
    assert len(arr) > 0
    assert arr == arr.reverse()

def test_list_is_zig_zag(arr: list) -> bool:
    assert len(arr) > 0
    for i in range(len(arr) - 1):
        try:
            assert(arr[i] % 2 != arr[i+1] % 2)
        except IndexError:
            pass

# Fill out the function bodies so the tests pass

"""
create_palindromic_list() -> list

Returns a list of length n that is a palindrome; i.e same
elements in same order in both directions
"""
def create_palindromic_list(n) -> list:
    return [1]*n


"""
create_zig_zag_list() -> list

Returns a list of length n that alternates each element between
odd and even
"""
def create_zig_zag_list(n) -> list:
    return [1,2]*(n//2)+[1]*(n%2)


if __name__ == "__main__":
    try:
        arr = create_palindromic_list()
        test_list_is_palindromic(arr)

        arr2 = create_zig_zag_list()
        test_list_is_zig_zag(arr2)
    except AssertionError:
        print("Test failed")
    
