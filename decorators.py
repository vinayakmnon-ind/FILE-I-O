# Define a generator function
def square_generator(limit):
  num = 1
  while num <= limit:
    yield num ** 2
    num += 1

# Use the generator to iterate over squares
for square in square_generator(16):
  print(square)