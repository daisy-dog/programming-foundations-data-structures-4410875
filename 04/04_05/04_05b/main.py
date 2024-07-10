def has_unique_characters(data):
    data_set = set(data)
    return len(data) == len(data_set)

    # if len(data) == len(data_set):
    #     return True
    # else:
    #     return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
