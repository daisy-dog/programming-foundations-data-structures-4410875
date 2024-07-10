from collections import deque

def convert_to_binary(num):
  if num <= 0:
    return
  binary_queue = deque()
  for n in range(1,num +1):
    # print(f"{n:b}")
    binary_queue.append(f"{n:0b}")
  return binary_queue

def print_binary_numbers(n):
  if n <= 0:
    return
  queue = deque()
  queue.append(1)
  for i in range(n):
    binary = queue.popleft()
    print(binary)
    queue.append(binary * 10)
    queue.append(binary * 10 + 1)



# print(convert_to_binary(6))
print_binary_numbers(6)
print('---------------')
print_binary_numbers(9)
print('---------------')
print_binary_numbers(0)
print('---------------')
print_binary_numbers(2)