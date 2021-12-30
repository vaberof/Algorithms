def binary_search(list, item):
    """Returns list`s index of input number for O(log2N) time"""
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [i for i in range(1, 10)]

my_list.sort()

print(binary_search(my_list, 5))
