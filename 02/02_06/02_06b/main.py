# Tuples are immutable array-like structures

point = (5,2)

print(point[0])
print(point[1])
x = point[0]
y = point[1]

def calculate_square_properties(side_length):
  area = side_length * side_length
  perimeter = 4 * side_length
  return (area, perimeter)

result = calculate_square_properties(5)
print(f"area = {result[0]}, permiter = {result[1]} ")