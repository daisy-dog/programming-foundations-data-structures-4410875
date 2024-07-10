def find_second_smallest(my_list):
    if not(my_list):
        return
    else:
        # return my_list[2]
        smallest = min(my_list)
        my_list.remove(smallest)
        return min(my_list)

print(find_second_smallest([5, 8, 3, 2, 6]))

def find_second_smallest2(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]

print(find_second_smallest2([5, 8, 3, 2, 6]))
print(find_second_smallest2([5, 8, 3]))
print(find_second_smallest2([5]))

def find_second_smallestv3(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest


print(find_second_smallestv3([5, 8, 3, 2, 6]))
print(find_second_smallestv3([5, 8, 3, 2, 6]))