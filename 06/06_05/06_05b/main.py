from collections import deque

def check_matching_parentheses(s):
  parens = deque()
  for char in s:
    if char == '(':
      parens.append(char)
    elif char == ')':
      if not parens:
        return False
      parens.pop()
  return len(parens) == 0



# print(check_matching_parentheses('hello(()'))
# print(check_matching_parentheses('hello(())'))
# print(check_matching_parentheses('hello(())'))

print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))

print(check_matching_parentheses("(hi(there"))
print(check_matching_parentheses("()ok)"))
print(check_matching_parentheses("((increment)"))
print(check_matching_parentheses(")linkedin()"))
