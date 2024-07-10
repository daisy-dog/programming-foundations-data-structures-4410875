# Key: State
# Value: Capital

state_to_capitals = {
  'Texas': 'Austin',
  'New York': 'Albany'
}

print(state_to_capitals['New York'])

for key in state_to_capitals.keys():
  print(key, state_to_capitals[key])

for key, value in state_to_capitals.items():
  print(key, value)